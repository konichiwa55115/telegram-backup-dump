import os

class Config:
   API_ID = int(17983098)
    API_HASH = "ee28199396e0925f1f44d945ac174f64"
    BOT_TOKEN = "6037424775:AAH6i1M9CII2ws7rTDKQJ3GAReJbiyFCmF0"
    LOGS_CHANNEL = int(os.environ.get("LOGS_CHANNEL", None))

class Var:
    currentuser = int()
    waitinglist = []
    idtodump = None
    startrange = 1
    stoprange = None
    dumpid = int()
    tagged = True
    currentpost = int()
    howmanyposts = int()
    postlist = []
    tasks = [None, None, None, None, None]
