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

    def check_group_score(self):
        groups = self.group_collection.find()
        pro_list=[]
        for group in groups:
            if group["leader"]["last_score"] == '00' and group['advisor'] not in pro_list:
                pro_list.append(group['advisor'])
        return pro_list

    def has_already_set_score(self):
        groups = self.group_collection.find()
        with open('has_score.txt','w') as f:
            for group in groups:
                if group["leader"]["last_score"] != '00':
                    f.write(f"group_id:{group['group_id']} group_leader:{group['leader']['name']} advisor:{group['advisor']}已評分\n")
        print('done!')

    def has_not_already_set_score(self):
        groups = self.group_collection.find()
        with open('has_no_score.txt','w') as f:
            for group in groups:
                if group["leader"]["last_score"] == '00':
                    f.write(f"group_id:{group['group_id']} group_leader:{group['leader']['name']} advisor:{group['advisor']}尚未評分\n")
        print('done!')

    def find_no_group_pro(self):
        groups = self.group_collection.find()
        pro_list=['李士修', '鄭瑞清', '李仁貴', '邱弘緯', '黃育賢', '陳建中', '曾恕銘', '李文達', '林信標', '范育成', '王多柏', '劉玉蓀', '余政杰', '林鼎然', '高立人', '黃士嘉', '胡心卉', '蔡偉和', '段裘慶', '孫卓勳', '曾德樟', '陳晏笙', '王紳', '譚巽言', '楊濠瞬', '潘孟鉉', '賴冠廷', '黃柏鈞', '李昭賢', '鍾明桉', '陳維昌', '曾柏軒']
        for group in groups:
            if group["advisor"] in pro_list:
                pro_list.remove(group["advisor"])
        return pro_list

    def find_group_info(self):
        group_id = input("輸入小組ID:")
        group = self.group_collection.find_one({"group_id":group_id})
        print(f"小組ID{group['group_id']}")
        print(f"小組組長{group['leader']['student_id']} {group['leader']['name']} 小組組長分數{group['leader']['last_score']}")
        for member in group['member']:
            print(f"姓名：{member['name']} 學號：{member['student_id']} 分數：{member['last_score']}")

if __name__ == "__main__":
    choice = 'start'
    while choice != "Q":
        choice = input("執行哪個功能?")
        if choice == '1':
            print(f"總共有{count().count_group()}組")
        elif choice == '2':
            print(f"有{count().check_interm_report()}組已繳交報告")
        elif choice == '3':
            print(f"有以下教授尚未評分{count().check_group_score()}")
        elif choice == '4':
            print(f"有以下教授沒有專題生{count().find_no_group_pro()}")
        elif choice == '5':
            count().has_already_set_score()
        elif choice == '6':
            count().has_not_already_set_score()
        elif choice == '7':
            count().find_group_info()