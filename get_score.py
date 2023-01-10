from pymongo import MongoClient
import csv

class score:
    def __init__(self):
        self.cluster = MongoClient("mongodb://localhost:27017")
        self.db = self.cluster["user_storage"]
        self.group_collection = self.db['group']
        self.file_name = ["304804_2022104_1.csv","304834_2022104_1.csv","307614_2022104_1.csv","307688_2022104_1.csv"]
        self.output_file_name = ["1.csv","2.csv","3.csv","4.csv"]
        self.output_csv = "score_output.csv"

    def get_all_score(self):
        groups = self.group_collection.find()
        with open(self.output_csv,'w',newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['學號','姓名','分數'])
            for group in groups:
                leader = group['leader']
                writer.writerow([leader['student_id'],leader['name'],leader['last_score']])
                for member in group['member']:
                    try:
                        writer.writerow([member['student_id'],member['name'],member['last_score']])
                    except:
                        print(member)
            
    def change_format(self):
        for input_file in self.file_name:
            with open(input_file,'r',newline='') as file:
                input_data = [row for row in csv.DictReader(file)]
                for student in input_data:
                    with open(self.output_csv,'r',newline='') as score_file:
                        rows = csv.DictReader(score_file)
                        for row in rows:
                            if row['學號'] == student['學號']: 
                                student['分數'] = row['分數']                                                              
                                break
                        if student['分數'] == '':
                            print(student)
                with open(input_file,'w',newline='') as output_file:
                    writer = csv.DictWriter(output_file,fieldnames=['班級','學號','姓名','分數'])
                    writer.writeheader()
                    writer.writerows(input_data)

                                



if __name__ == "__main__":
    score().get_all_score()
    score().change_format()
