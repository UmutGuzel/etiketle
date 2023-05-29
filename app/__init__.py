from pymongo import MongoClient
MONGODB_URI = ""

client = MongoClient(MONGODB_URI, maxPoolSize=50, minPoolSize=10)