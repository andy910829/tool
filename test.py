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
            self.check_name(group_leader_name,
                            group_leader_id, group["group_id"])
            for member in group["member"]:
                member_id = member["student_id"]
                member_name = member["name"]
                self.check_name(member_name, member_id, group["group_id"])

    def check_name(self, user_name, user_id, group_id):
        user = self.user_collection.find_one({"student_id": user_id})
        if user["name"] != user_name:
            print(user_id, user_name)
            change = input(
                f"Do you want to change {user_name} to {user['name']}? (y/n)")
            if change == "y":
                if user['user_identity'] == 'group_leader':
                    self.group_collection.update_one(
                        {"group_id": user_id}, {"$set": {"group_leader.name": user['name']}})

    def check_judge(self):
        for group in self.group_collection.find():
            for group_judge in group['judge']:
                judge = self.user_collection.find_one(
                    {"name": group_judge['name']})
                if group['group_id'] not in judge['groups']:
                    print(group['group_id'], judge['name'])

    def check_group(self):
        for user in self.user_collection.find({"acedemic_year": "112"}):
            cnt = 0
            group = self.group_collection.find_one({"group_id":user['group_id']})
            try:
                for member in group['member']:
                    if member['student_id'] == user['student_id']:
                        cnt += 1
                if cnt > 1:
                    print(user['group_id'], user['student_id'])
            except:
                print(user['group_id'])
                print(group)


if __name__ == '__main__':
    tool().check_group()
