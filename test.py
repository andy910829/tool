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
            "type": "admin",
            "name":"潘孟鉉"
        }
        self.collection.update_one({"account":admin["account"]},{"$set":admin})
        print("done!")
    
    def update_pro(self):
        pro_info = self.collection.find_one({"account":"mspan@ntut.edu.tw"})
        pro_info["type"] = "admin"
        self.collection.update_one({"account":"mspan@ntut.edu.tw"},{"$set":pro_info})
        print("change pro info done!!")

if __name__ == "__main__":
    tool().insert_admin()
    tool().update_pro()
