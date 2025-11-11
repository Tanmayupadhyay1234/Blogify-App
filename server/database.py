import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI")

client = None
db = None

def get_database():
    global client, db
    if db is None:
        client = MongoClient(
            MONGODB_URI,
            tlsAllowInvalidCertificates=True,
            serverSelectionTimeoutMS=10000
        )
        db = client.get_database("blog_platform")
    return db

def get_collection(name):
    database = get_database()
    return database[name]
