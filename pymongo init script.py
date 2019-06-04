import pymongo
from pymongo import MongoClient


myClient = MongoClient()
# client = MongoClient("localhost", 27017)
# client = MongoClient('mongodb://localhost:27017/')

db = myClient.mydb
# db = myClient["mydb"]

users = db.users
user1 = {"username": "vishrutjha10", "password": "Reallysecure445", "favorite_number": 710, "hobbies": ['python', 'soccer']}
user_id = users.insert_one(user1).inserted_id
print(user_id)
