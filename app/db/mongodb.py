from pymongo import MongoClient
from os import getenv

MONGO_URL = getenv('MONGODB_URI')

try:
    mongo_client = MongoClient(MONGO_URL)
    mongo_db = mongo_client["sms_management"]
    config_collection = mongo_db["sms_config"]
except :
    print("mongodb error")