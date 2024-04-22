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
        data = collection.find_one({"Register Number": int(regNo)})

        return data["sem"][str(sem)]

    def mark_attendance(self, data: list, sem: int):
        attendance_collection = self.db_handler["attendance"]

        # data = [
        #     {
        #         "Register Number": 714022104076,
        #         "sem": sem,
        #         "attendance": {"subject": "PQT", "status": "Present"},
        #     },
        #     {
        #         "Register Number": 71402210495,
        #         "sem": sem,
        #         "attendance": {"subject": "PQT", "status": "OD"},
        #     },
        #     {
        #         "Register Number": 714022104114,
        #         "sem": sem,
        #         "attendance": {"subject": "PQT", "status": "Absent"},
        #     },
        # ]
        
        for _student in data:
            _old_attendance = attendance_collection.find_one(
                {"Register Number": _student["Register Number"]}
            )
            _subject = _old_attendance["sem"][str(sem)]
            
            try:
                _subject[str(_student["attendance"]["subject"]).lower()]["dates"].pop("")
            except KeyError:
                pass
            try:
                if str(_student["attendance"]["status"]).lower() == "present" and _subject[str(_student["attendance"]["subject"]).lower()]["dates"][str(datetime.now().date())] == "absent":
                    _subject[str(_student["attendance"]["subject"]).lower()]["attendance"] += 1
                elif str(_student["attendance"]["status"]).lower() == "od" and _subject[str(_student["attendance"]["subject"]).lower()]["dates"][str(datetime.now().date())] == "absent":
                    _subject[str(_student["attendance"]["subject"]).lower()]["attendance"] += 1
                elif str(_student["attendance"]["status"]).lower() == "absent" and _subject[str(_student["attendance"]["subject"]).lower()]["dates"][str(datetime.now().date())] == "od":
                    _subject[str(_student["attendance"]["subject"]).lower()]["attendance"] -= 1
                elif str(_student["attendance"]["status"]).lower() == "absent" and _subject[str(_student["attendance"]["subject"]).lower()]["dates"][str(datetime.now().date())] == "present":
                    _subject[str(_student["attendance"]["subject"]).lower()]["attendance"] -= 1
                _subject[str(_student["attendance"]["subject"]).lower()]["dates"][str(datetime.now().date())] = str(_student["attendance"]["status"]).lower()
            except KeyError:
                _subject[str(_student["attendance"]["subject"]).lower()]["dates"][str(datetime.now().date())] = str(_student["attendance"]["status"]).lower()
                if str(_student["attendance"]["status"]).lower() == "present":
                    _subject[str(_student["attendance"]["subject"]).lower()]["attendance"] += 1
                elif str(_student["attendance"]["status"]).lower() == "od":
                    _subject[str(_student["attendance"]["subject"]).lower()]["attendance"] += 1

            attendance_collection.update_one({"Register Number" : _old_attendance["Register Number"]}, {"$set" : {f"sem.{sem}" : _subject}})
        return {"marked attendance" : "success"}

    def insert_attendance(self):

        attendance_collection = self.db_handler["attendance"]

        student_collection = self.db_handler["students"]

        rawData = list(student_collection.find())
        dataN = []

        year_map = {
            "I": 1,
            "II": 2,
            "III": 3,
            "IV": 4,
            1: "I",
            2: "II",
            3: "III",
            4: "IV",
        }

        for document in rawData:
            passing_out = int(document["Academic Year"].split()[0])
            current_year = abs(passing_out - datetime.now().year)
            document.pop("_id")
            subjects = db_handler["subjects"].find_one({"year": year_map[current_year]})

            subject_attendance_map = {
                str(current_year): {
                    subject: {"attendance": 0, "dates": {"": ""}}
                    for subject in subjects["subjects"]
                }
            }

            temp = {
                "Roll Number": document["Roll Number"],
                "Register Number": document["Register Number"],
                "sem": subject_attendance_map,
            }
            dataN.append(temp)
        status = {}
        try:
            for _student in dataN:
                if (
                    attendance_collection.find_one(
                        {"Register Number": _student["Register Number"]}
                    )
                    is not None
                ):
                    old_student = attendance_collection.find_one(
                        {"Register Number": _student["Register Number"]}
                    )
                    old_student["sem"][str(current_year)] = _student["sem"][
                        str(current_year)
                    ]

                    attendance_collection.update_one(
                        {"Register Number": _student["Register Number"]},
                        {"$set": {"sem": old_student["sem"]}},
                    )
                    status = {"info": "updated successfully"}
                else:
                    attendance_collection.insert_one(_student)
                    status = {"info": "inserted successfully"}
        except Exception as e:
            status = {"info": "failed to insert", "error": str(e)}

        return status

    def update_timetable(self, timetable_data: list) -> dict:
        timetable_collection = self.db_handler["timetables"]

        try:
            for _class in timetable_data:
                if (
                    timetable_collection.find_one(
                        {"year": _class["year"], "section": _class["section"]}
                    )
                    is not None
                ):
                    timetable_collection.find_one_and_replace(
                        {"year": _class["year"], "section": _class["section"]}, _class
                    )
                else:
                    timetable_collection.insert_one(_class)
            return {"inserted": True}
        except Exception as e:
            return {"inserted": False, "error": str(e)}

    def update_subjects(self, subject_data: list) -> dict:
        subject_collection = self.db_handler["subjects"]

        try:
            for _year in subject_data:
                if subject_collection.find_one({"year": _year["year"]}) is not None:
                    subject_collection.find_one_and_replace(
                        {"year": _year["year"]}, _year
                    )
                else:
                    subject_collection.insert_one(_year)
            return {"inserted": True}
        except Exception as e:
            return {"error": str(e)}


db = EduDatabase("edumatrics")
db.create_connection("navin82005", "navin82005")
db_handler = db.get_database_handler()

student_collection = db_handler["students"]
