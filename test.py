from pymongo import MongoClient


class tool:
    def __init__(self):
        self.cluster = MongoClient("mongodb://localhost:27017")
        self.db = self.cluster["user_storage"]
        self.user_collection = self.db["user"]
        self.group_collection = self.db["group"]

    def main(self):
        groups = self.group_collection.find()
        for group in groups:
            group_leader_id = group["leader"]["student_id"]
            group_leader_name = group["leader"]["name"]
            self.check_name(group_leader_name, group_leader_id,group["group_id"])
            for member in group["member"]:
                member_id = member["student_id"]
                member_name = member["name"]
                self.check_name(member_name, member_id, group["group_id"])

    def check_name(self ,user_name, user_id, group_id):
        user = self.user_collection.find_one({"student_id": user_id})
        if user["name"] != user_name:
            print(user_id, user_name)
            change = input(f"Do you want to change {user_name} to {user['name']}? (y/n)")
            if change == "y":
                if user['user_identity'] == 'group_leader':
                    self.group_collection.update_one({"group_id": user_id}, {"$set": {"group_leader.name": user['name']}})

if __name__ == '__main__':
    tool().main()

