from os import environ 

class Config:
    API_ID = environ.get("API_ID", "25121213")
    API_HASH = environ.get("API_HASH", "b734dcc45da130a8156e2be836594706")
    BOT_TOKEN = environ.get("BOT_TOKEN", "7574864308:AAG0qTatxpgShwUVly3BA8ev6ViFa8HqL-4") 
    BOT_SESSION = environ.get("BOT_SESSION", "Pragyan") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://AvyukthX:AvyukthX@bot.ctdiudr.mongodb.net/?retryWrites=true&w=majority")
    DATABASE_NAME = environ.get("DATABASE_NAME", "PragyanForwardBot")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '5464921200').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
