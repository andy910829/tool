from pymongo import MongoClient

class count:
    def __init__(self):
        self.cluster = MongoClient("mongodb://localhost:27017")
        self.db = self.cluster["user_storage"]
        self.group_collection = self.db['group']
    
    def count_group(self):
        group = self.group_collection.find()
        cnt = 0
        for g in group:
            cnt+=1
        return cnt

    def check_interm_report(self):
        group = self.group_collection.find()
        cnt = 0
        for g in group:
            if g['interm_report']['file_path'] != '':
                cnt+=1
        return cnt
if __name__ == "__main__":
    print('總共有'+count().count_group()+'組')
    print('已繳交期中報告有'+count().check_interm_report()+'組')
