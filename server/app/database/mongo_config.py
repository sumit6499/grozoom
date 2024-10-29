from pymongo import MongoClient
from app.core.config import settings

client = None

def connect_to_mongodb():
    global client
    client = MongoClient(settings.MONGODB_URI)

def close_mongodb_connection():
    global client
    if client:
        client.close()

def get_country_operators_collection():
    global client
    db = client[settings.MONGODB_DB]
    return db["country_operators"]