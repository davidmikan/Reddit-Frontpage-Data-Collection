from config import *
import threading
import time
import praw
import pg
from signal import signal, SIGINT
import sys
import logger

class Scheduler:
    iterations = 0
    def __init__(self, reddits:list, subs:list):
        self.target_time = time.time()
        self.groups = {}
        self.reddits = reddits
        self.subs = subs

    def add_groups(self, reddit):
        for sub in self.subs:
            group = pg.PostGroup(sub)
            group.collect(reddit)
            group.update(reddit)
            self.groups[group.id] = group

    def iterate(self):
        reddit = self.reddits[self.iterations % len(self.reddits)]
        self.iterations += 1
        logger.logbr()
        self.target_time = self.target_time + INTERVAL_M * 60
        popped = []
        for g_id in self.groups:
            try:
                self.groups[g_id].update(reddit)
            except Exception:
                self.groups[g_id].save()
                popped.append(g_id)
        for pop in popped: self.groups.pop(pop)
        self.add_groups(reddit)
        print(f"next update at {time.strftime('%H:%M:%S', time.localtime(self.target_time))}")
        
    def exit(self, _, __):
        for group in self.groups:
            self.groups[group].save(f'unfinished_datasets/{group}{time.time()}.json')
        sys.exit(0)

    def mainloop(self):
        while True:
            if time.time() > self.target_time:
                threading.Thread(target=self.iterate).run()
            time.sleep(60)

if __name__ == '__main__':
    m_sched = Scheduler([praw.Reddit(DEFAULT_PROFILE), praw.Reddit(ALT_PROFILE)], SUBREDDITS)
    signal(SIGINT, m_sched.exit)
    m_sched.mainloop()