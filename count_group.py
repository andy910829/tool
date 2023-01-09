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
            if group["leader"]["last_score"] != '00':
                print(f"group_id:{group['group_id']} group_leader:{group['leader']['name']} advisor:{group['advisor']}已評分")
            elif group['advisor'] not in pro_list:
                pro_list.append(group['advisor'])
                print(f"group_id:{group['group_id']} group_leader:{group['leader']['name']} advisor:{group['advisor']}尚未評分")
        return pro_list

    def find_no_group_pro(self):
        groups = self.group_collection.find()
        pro_list=['李士修', '鄭瑞清', '李仁貴', '邱弘緯', '黃育賢', '陳建中', '曾恕銘', '李文達', '林信標', '范育成', '王多柏', '劉玉蓀', '余政杰', '林鼎然', '高立人', '黃士嘉', '胡心卉', '蔡偉和', '段裘慶', '孫卓勳', '曾德樟', '陳晏笙', '王紳', '譚巽言', '楊濠瞬', '潘孟鉉', '賴冠廷', '黃柏鈞', '李昭賢', '鍾明桉', '陳維昌', '曾柏軒']
        for group in groups:
            if group["advisor"] in pro_list:
                pro_list.remove(group["advisor"])
        return pro_list

if __name__ == "__main__":
    choice = 'start'
    while choice != "Q":
        print("1.count_group  2.check_interm_report  3.check_group_score 4.find_no_group_pro")
        choice = input("執行哪個功能?")
        if choice == '1':
            print(f"總共有{count().count_group()}組")
        elif choice == '2':
            print(f"有{count().check_interm_report()}組已繳交報告")
        elif choice == '3':
            print(f"有以下教授尚未評分{count().check_group_score()}")
        elif choice == '4':
            print(f"有以下教授沒有專題生{count().find_no_group_pro()}")