from datetime import datetime

def log(msg, pgid=None):
    timestr = datetime.now().strftime('[%H:%M:%S]')
    if pgid is not None:
        print(f"{timestr} ({pgid}) {msg}")
    else:
        print(f"{timestr} {msg}")

def logbr():
    print('-'*20)