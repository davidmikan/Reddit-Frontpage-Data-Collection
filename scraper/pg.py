import praw
import json
from datetime import datetime, timezone
from config import *
from logger import log # got waaaays to go

class PostGroup:
    instances = 0
    def __init__(self, from_sub:str, rem_saves:int=SAVES, from_path:str=None):
        PostGroup.instances += 1
        self.id = str(PostGroup.instances) + ':' + from_sub
        self.from_sub = from_sub
        self.rem_saves = rem_saves
        self.update_filters = {}
        self.posts = {}
        self.from_path = from_path

    def add_post(self, submission):
        self.posts[submission.id] = {attr: getattr(submission, attr) for attr in ATTR_STATIC}
        self.posts[submission.id]['updates'] = {}

    def collect(self, reddit, limit=MAX_GROUPSIZE):
        timestamp = datetime.timestamp(datetime.now(timezone.utc))
        for submission in reddit.subreddit(self.from_sub).new(limit=limit):
            if submission.created_utc + MAX_TIMEDIF*60 < timestamp: 
                continue
            self.add_post(submission)
        self.collected_utc = timestamp
        log(f"collected {len(self.posts)} posts from {self.from_sub}", self.id)

    def update(self, reddit):
        if self.rem_saves <= 0:
            raise Exception("No further saves remaining")
        log(f"updating posts, updates left: {self.rem_saves}", self.id)
        timestamp = datetime.timestamp(datetime.now(timezone.utc))
        try:
            sub = reddit.subreddit(self.from_sub)
        except Exception:
            log('couldn\'t be saved, ' + self.jsonify(), self.id)
            return
        filters = [
            {_.id for _ in sub.rising(limit=MAX_FILTER)}, 
            {_.id for _ in sub.hot(limit=MAX_FILTER)}
        ]
        self.update_filters[timestamp] = [list(_) for _ in filters]
        for p_id, post in self.posts.items():
            try: 
                submission = reddit.submission(p_id)
                update = {}
                for attr in ATTR_VARIABLE:
                    update[attr] = getattr(submission, attr)
                # if submission is rising/hot (ergo interesting)
                update['rising'] = p_id in filters[0]
                update['hot'] = p_id in filters[1]
                if update['rising']: log(f"{p_id} is in Rising! Upvotes: {update['score']}, {update['upvote_ratio']}")
                if update['hot']:
                    log(f"{p_id} is in Hot!!! Upvotes: {update['score']}, Ratio: {update['upvote_ratio']}")
                # -
                post['updates'][timestamp] = update
            except Exception as e:
                log(f"failed to update {p_id}, error: {e}", self.id)
                self.posts.pop()
        self.rem_saves -= 1
        log(f"finished updating posts", self.id)

    def next(self):
        try:
            self.update()
        except:
            self.save()

    def jsonify(self):
        j_dict = {}
        j_dict['collected_utc'] = self.collected_utc
        j_dict['from_sub'] = self.from_sub
        j_dict['rem_saves'] = self.rem_saves
        j_dict['update_filters'] = self.update_filters
        j_dict['posts'] = self.posts
        return json.dumps(j_dict)

    def save(self, path=''):
        path = path or self.from_path or f"{SAVE_PATH}{self.from_sub}_{datetime.now(timezone.utc).strftime('%m-%d-%H-%M')}.json"
        if not path.endswith('.json'): path += '.json'
        try:
            jstr = self.jsonify()
        except Exception as e:
            log(f"failed to jsonify", self.id)
            return
        with open(path, 'w') as f:
            f.write(self.jsonify())
            log(f"saved to {path}", self.id)

    @staticmethod
    def load(path:str):
        with open(path) as f:
            raw_dict = json.load(f)
        pg = PostGroup(raw_dict['from_sub'], rem_saves=raw_dict['rem_saves'], from_path=path)
        pg.collected_utc = raw_dict['collected_utc']
        pg.update_filters.update(raw_dict['update_filters'])
        pg.posts = raw_dict['posts']
        return pg