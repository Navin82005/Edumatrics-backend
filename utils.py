from pymongo import MongoClient
import json
from datetime import datetime


class EduDatabase:
    def __init__(self, db_name: str = None):
        self.database_name = db_name
        self.client = None
        self.db_handler = None

    def create_connection(self, username: str, password: str):
        try:
            self.client = MongoClient(
                f"mongodb+srv://{username}:{password}@project-hub.xrmnjxs.mongodb.net/{self.database_name}?retryWrites=true&w=majority&appName=project-hub"
            )
        except Exception as e:
            raise ValueError("Error in connecting to MongoDB: ")

    def get_database_handler(self):
        self.db_handler = self.client[self.database_name]
        return self.db_handler

    def insert_new_students(self, student_data: list):
        collection = db_handler["students"]
        dict_data = {x: [] for x in student_data[0]}
        dict_keys = list(dict_data.keys())
        for _d in student_data[1:]:
            temp = {dict_keys[i]: _d[i] for i in range(len(_d))}
            collection.insert_one(temp)
            print(temp)

    def remove_all_students(self, data):
        collection = db_handler["students"]
        collection.delete_many({})

    def fetch_internals(self, department: str, sem: int, iit: int):
        internals_collection = self.db_handler["results"]

        return internals_collection.find({"department": department, "sem": sem})

    def update_internals(self, data):
        internals_collection = self.db_handler["results"]

        data_json = json.dumps(data)
        data_dict = json.loads(data_json)

        acknowledgement = internals_collection.insert_one(data_dict)
        return {"status": "200 ok", "acknowledgement": acknowledgement}

    def remove_all_results(self):
        collection = db_handler["results"]
        collection.delete_many({})

    def get_attendance(self, sem, regNo):
        data = {}

        """
        attendance = {
            
        }
        """

        collection = self.db_handler["attendance"]
        data = collection.find({"registerNumber": regNo, "sem": sem})
        print(data)
        return data

    def update_attendance(self, data, sem):
        attendance_collection = self.db_handler["attendance"]

        data = [
            {
                "registerNumber": 714022104076,
                "sem": sem,
                "attendance": {"subject": "PQT", "status": "Present"},
            },
            {
                "registerNumber": 71402210495,
                "sem": sem,
                "attendance": {"subject": "PQT", "status": "OD"},
            },
            {
                "registerNumber": 714022104114,
                "sem": sem,
                "attendance": {"subject": "PQT", "status": "Absent"},
            },
        ]

        # for i in data:
        #     attendance_collection.update_one({"registerNumber": i["registerNumber"], "sem": i["sem"], "attendance":i[]})

    def insert_attendance(self):
        attendance_collection = self.db_handler["attendance"]

        data = [
            {
                "register_number": 714022104076,
                "sem": {
                    "1": {
                        "internals": {
                            "1": {"PQT": 90, "ADB": 90, "DAA": 80, "AJP": 95, "IP": 96},
                            "2": {"PQT": 90, "ADB": 90, "DAA": 80, "AJP": 95, "IP": 96},
                            "3": {"PQT": 90, "ADB": 90, "DAA": 80, "AJP": 95, "IP": 96},
                        },
                        "overall": {
                            "PQT": 90,
                            "ADB": 90,
                            "DAA": 80,
                            "AJP": 95,
                            "IP": 96,
                        },
                    }
                },
            },
            {
                "register_number": 714022104095,
                "sem": {
                    "1": {
                        "internals": {
                            "1": {"PQT": 90, "ADB": 90, "DAA": 80, "AJP": 95, "IP": 96},
                            "2": {"PQT": 90, "ADB": 90, "DAA": 80, "AJP": 95, "IP": 96},
                            "3": {"PQT": 90, "ADB": 90, "DAA": 80, "AJP": 95, "IP": 96},
                        },
                        "overall": {
                            "PQT": 90,
                            "ADB": 90,
                            "DAA": 80,
                            "AJP": 95,
                            "IP": 96,
                        },
                    }
                },
            },
        ]

        student_collection = self.db_handler["students"]

        rawData = list(student_collection.find())
        dataN = []
        print("Students inside utils.insert_attendance", rawData)
        for document in rawData:
            passing_out = int(rawData["Academic Year"].split()[0])
            current_year = passing_out - datetime.now().year
            document.pop("_id")
            print("current_year", current_year)
            semData = {}
            for year in range(1, passing_out + 1):
                semData[f"{year}"] = 
            temp = {
                "Roll Number": document["Roll Number"],
                "Register Number": document["Register Number"],
                "sem": {},
            }
            dataN.append(temp)

        # status = attendance_collection.insert_many(data)
        # print(status)
        return dataN


db = EduDatabase("edumatrics")
db.create_connection("navin82005", "navin82005")
db_handler = db.get_database_handler()

student_collection = db_handler["students"]

# print(
#     student_collection.insert_one(
#         {
#             "name": "Naveen N",
#             "department": "CSE",
#             "dob": "08-01-2004",
#         }
#     )
# )
