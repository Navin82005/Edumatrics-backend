from auth_api.models import Student
from utils import db_handler, db


def getStudents(department: str, sem: int, iit: int) -> list:
    # data = []
    # DATA TEMPLATE

    data = {
        "year": 2,
        "name": "Naveen N",
        "roll_number": "22CS095",
        "register_number": 714022104095,
        "department": "cse",
        "sem": {
            "1": {
                "attendance": 90,
                "internals": {
                    "1": {
                        "attendance": 90,
                        "subjects": {
                            "PQT": 90,
                            "ADB": 90,
                            "AJP": 90,
                            "DAA": 90,
                            "IP": 90,
                        },
                    },
                    "2": {
                        "attendance": 90,
                        "subjects": {
                            "PQT": 90,
                            "ADB": 90,
                            "AJP": 90,
                            "DAA": 90,
                            "IP": 90,
                        },
                    },
                    "3": {
                        "attendance": 90,
                        "subjects": {
                            "PQT": 90,
                            "ADB": 90,
                            "AJP": 90,
                            "DAA": 90,
                            "IP": 90,
                        },
                    },
                },
            },
            "2": {
                "internals": {
                    "1": {
                        "attendance": 90,
                        "subjects": {
                            "PQT": 90,
                            "ADB": 90,
                            "AJP": 90,
                            "DAA": 90,
                            "IP": 90,
                        },
                    },
                    "2": {
                        "attendance": 90,
                        "subjects": {
                            "PQT": 90,
                            "ADB": 90,
                            "AJP": 90,
                            "DAA": 90,
                            "IP": 90,
                        },
                    },
                    "3": {
                        "attendance": 90,
                        "subjects": {
                            "PQT": 90,
                            "ADB": 90,
                            "AJP": 90,
                            "DAA": 90,
                            "IP": 90,
                        },
                    },
                },
            },
            "3": {
                "internals": {
                    "1": {
                        "attendance": 90,
                        "subjects": {
                            "PQT": 90,
                            "ADB": 90,
                            "AJP": 90,
                            "DAA": 90,
                            "IP": 90,
                        },
                    },
                    "2": {
                        "attendance": 90,
                        "subjects": {
                            "PQT": 90,
                            "ADB": 90,
                            "AJP": 90,
                            "DAA": 90,
                            "IP": 90,
                        },
                    },
                    "3": {
                        "attendance": 90,
                        "subjects": {
                            "PQT": 90,
                            "ADB": 90,
                            "AJP": 90,
                            "DAA": 90,
                            "IP": 90,
                        },
                    },
                },
            },
        },
    }

    # data = {
    #     "name": "Naveen N",
    #     "roll_number": "22CS095",
    #     "register_number": 714022104095,
    # }

    # print(db.update_internals(data))
    # db.remove_all_results()
    results_data = list(db.fetch_internals(department, sem, iit))

    print("results_data", results_data)

    for i in results_data:
        i.pop("_id")
    #     for j in i:
    #         print(j, i[j])

    # students = Student.objects.filter(department=department)

    # for i in students:
    #     data.append(i.get_main_data())

    return results_data
