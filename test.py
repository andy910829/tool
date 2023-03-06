from pymongo import MongoClient


class tool:
    def __init__(self):
        self.cluster = MongoClient("mongodb://localhost:27017")
        self.db = self.cluster["user_storage"]
        self.collection = self.db["user"]

    def insert_admin(self):
        admin = {
            "account": "andy625018171@gmail.com",
            "password": "9ceae5f376d2713c47b7b1d520fc3062e8eeb5689dcbffe424e7d697d0d4f8df",
            "token": "",
            "type": "admin"
        }
        self.collection.insert_one(admin)
        print("done!")

if __name__ == "__main__":
    tool().insert_admin()
