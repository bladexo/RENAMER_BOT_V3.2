import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "6918704487:AAHqzEF292uKEmUlzOv4F2n-OQQgE7y8AHU")

API_ID = int(os.environ.get("API_ID", "25803426"))

API_HASH = os.environ.get("API_HASH", "291b6bea4848d7606c0d3213c317b430")

STRING = os.environ.get("STRING", "")


bot = Client(

           "Renamer",

           bot_token=TOKEN,

           api_id=API_ID,

           api_hash=API_HASH,

           plugins=dict(root='plugins'))
           

if STRING:
    apps = [Client2,bot]
    for app in apps:
        app.start()
    idle()
    for app in apps:
        app.stop()
    
else:
    bot.run()
