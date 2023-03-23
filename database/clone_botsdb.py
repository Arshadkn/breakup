import pymongo
import requests
from info import DATABASE_URI, DATABASE_NAME




client = pymongo.MongoClient(DATABASE_URI)
db = client[DATABASE_NAME]
bots_col = db["bots"]

async def save_bot_details(bot.username, bot_token):
    
  

    # Parse the response to extract the bot details
    

