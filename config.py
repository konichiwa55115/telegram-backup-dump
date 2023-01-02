import os

class Config:
   API_ID = int(os.environ.get("API_ID"))
    API_HASH = os.environ.get("API_HASH")
    BOT_TOKEN = os.environ.get("BOT_TOKEN")
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
