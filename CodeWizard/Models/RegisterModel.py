import pymongo, bcrypt
from pymongo import MongoClient


class RegisterModel:
    def __init__(self):
        self.client = MongoClient()
        self.db = self.client.codewizard
        self.Users = self.db.users

    def insert_user(self, data):
        hashed = bcrypt.hashpw(data.password.encode(), bcrypt.gensalt())
        id = self.Users.insert({"username": data.username, "password": hashed, 'email': data.email, 'name': data.name,
                                "avatar": "", "background": "", "about": "", "hobbies": "", "Birthday": ""})
        print("uid is", id)
        myuser = self.Users.find_one({"username": data.username})

        if bcrypt.checkpw("admin".encode(), myuser['password']):
            print("this matches")
