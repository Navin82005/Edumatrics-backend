from pymongo import MongoClient
import json


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

        return internals_collection.find(
            {"department": department, "sem": sem}
        )  # "sem": {sem: iit}})

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

        collection = db_handler["attendance"]
        return collection.find()

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
