import pymongo
import datetime
from pymongo import MongoClient


client = MongoClient()
# client = MongoClient("localhost", 27017)
# client = MongoClient('mongodb://localhost:27017/')

db = client.mydb
# db = myClient["mydb"]

Users = db.users
user1 = {"username": "vishrutjha10", "password": "Reallysecure445", "favorite_number": 710, "hobbies": ['python', 'soccer']}
user_id = Users.insert_one(user1).inserted_id
print(user_id)

# bulk insert
users = [{"username": "third", "password": "duh12345678"}, {"username": "fourth", "password": "duhBE12345678"},
         {"username": "5th", "password": "FOYTH_duh12345678"}]

inserted = Users.insert_many(users)
print(inserted.inserted_ids)

# counting documents
print("Documents", Users.find().count())
print("710:", Users.find({"favorite_number": 710}).count())
print("710 and vishrutjha10", Users.find({"favorite_number": 710, "username": "vishrutjha10"}).count())
# count is deprecated

current_date = datetime.datetime.now()
print(current_date)
old_date = datetime.datetime(2009, 8, 28)
uid = Users.insert({'username': 'ids_fotowale', 'dob': old_date, 'today': current_date})
print(">=", current_date, ":", Users.find({'today': {"$gte": old_date}}).count())
# gt: Greater than, gte: >=, lt: <, lte: <=, $exists: boolean true
print(Users.find({'today': {'$exists': True}}).count())
print("!= ids_fotowale:", Users.find({"username": {"$ne": "ids_fotowale"}}).count())

# Indexing for SCALABILITY
# index for username
# db.users.create_index([("username", pymongo.ASCENDING)], unique=True)
# db.users.create_index([("username", pymongo.ASCENDING)])
print("Index unique", db.users.create_index([("username", pymongo.ASCENDING)], unique=True))
print("index not unique", db.users.create_index([("username", pymongo.ASCENDING)]))
