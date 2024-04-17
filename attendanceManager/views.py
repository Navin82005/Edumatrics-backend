from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import LectureHall, LectureHallAttadence
from django.http import JsonResponse
import json
from datetime import datetime
from auth_api.models import Student
from .serializers import (
    get_period_cell,
    set_cell,
    get_cell_data,
    get_subject_attendance,
)

from utils import db


# Create your views here.
class GetStudents(APIView):

    def get(self, request, *args, **kwargs):
        # lectureHall = request.GET["lh"]
        _now_time = kwargs["dateTime"]
        lectureHall = _now_time.split(",")[1]
        print("GetStudents lectureHall", lectureHall)
        _now_time = _now_time.split(",")[0]
        print(lectureHall)
        if LectureHall.objects.filter(className=lectureHall) != None:
            hallData = LectureHall.objects.get(className=lectureHall)
            rawData = hallData.names.all()

            cell = get_period_cell(lectureHall, _now_time=_now_time)
            _period = cell[1]

            data = []

            for x in rawData:
                data += [
                    {
                        "name": x.name,
                        "rollNumber": x.rollNumber,
                        "isPresent": False,
                        "isOD": False,
                    }
                ]

            print("Period", _period)
            date = datetime.now().date()
            for i in data:
                temp = LectureHallAttadence.objects.filter(
                    mainName=i["name"], date=date
                )
                if list(temp) != []:
                    print("get_period_cell(lectureHall)[0]", cell)
                    cell_data = get_cell_data(cell=cell[0], instance=temp[0])
                    if cell_data != None:
                        i["isPresent"] = cell_data["present"]
                        i["isOD"] = cell_data["od"]

            return Response(
                {
                    "body": {"data": data, "period": _period},
                    "total": len(data),
                    "status": status.HTTP_200_OK,
                },
            )
        else:
            return Response(
                {
                    "Status": "Failed",
                },
            )

    def post(self, request, *args, **kwargs):
        lectureHall = request.POST["lh"]
        _now_time = kwargs["dateTime"]
        print(lectureHall)
        if LectureHall.objects.filter(className=lectureHall) != None:
            hallData = LectureHall.objects.get(className=lectureHall)
            rawData = hallData.names.all()

            cell = get_period_cell(lectureHall, _now_time=_now_time)
            _period = cell[1]

            data = []

            for x in rawData:
                data += [
                    {
                        "name": x.name,
                        "rollNumber": x.rollNumber,
                        "isPresent": False,
                        "isOD": False,
                    }
                ]

            print("Period", _period)
            date = datetime.now().date()
            for i in data:
                temp = LectureHallAttadence.objects.filter(
                    mainName=i["name"], date=date
                )
                if list(temp) != []:
                    print("get_period_cell(lectureHall)[0]", cell)
                    cell_data = get_cell_data(cell=cell[0], instance=temp[0])
                    print("cell_data", cell_data)
                    if cell_data != None:
                        i["isPresent"] = cell_data["present"]
                        i["isOD"] = cell_data["od"]

            return Response(
                {
                    "body": {"data": data, "period": _period},
                    "total": len(data),
                    "status": status.HTTP_200_OK,
                },
            )
        else:
            return Response(
                {
                    "Status": "Failed",
                },
            )


class markAttendance(APIView):
    def get(self, request, *args, **kwargs):
        period = kwargs["course"]
        lectureHall = kwargs["lh"]
        data = [
            {
                "name": "Kalandhar Naina Mohammed S",
                "class": "2 CSE - B",
                "rollNumber": "22CS060",
                "isPresent": True,
                "isOD": False,
            },
            {
                "name": "Kishore V",
                "class": "2 CSE - B",
                "rollNumber": "22CS070",
                "isPresent": False,
                "isOD": False,
            },
            {
                "name": "Madhan G",
                "class": "2 CSE - B",
                "rollNumber": "22CS076",
                "isPresent": False,
                "isOD": False,
            },
            {
                "name": "Naveen N",
                "class": "2 CSE - B",
                "rollNumber": "22CS095",
                "isPresent": True,
                "isOD": False,
            },
            {
                "name": "Rahulnisanth M",
                "class": "2 CSE - B",
                "rollNumber": "22CS114",
                "isPresent": True,
                "isOD": False,
            },
            {
                "name": "Ranjith S",
                "class": "2 CSE - B",
                "rollNumber": "22CS118",
                "isPresent": True,
                "isOD": False,
            },
        ]

        _cell = get_period_cell(data[0]["class"])
        print("cell", _cell)
        dateTime = datetime.now().date()

        for i in data:
            _class = LectureHall.objects.get(className=i["class"])
            # print(_class)
            _student = Student.objects.get(name=i["name"])

            if i["isPresent"]:
                i["isPresent"] = period.upper() + ":PRESENT"
            elif i["isOD"]:
                i["isPresent"] = period.upper() + ":OD"
            else:
                i["isPresent"] = period.upper() + ":ABSENT"

            stud = LectureHallAttadence.objects.filter(
                mainName=i["name"], date=dateTime
            )
            if list(stud) != []:
                print("attendanceManager.views stud:", stud)
                set_cell(i["isPresent"], _cell, list(stud))

            else:
                temp = LectureHallAttadence.objects.create(
                    h1=i["isPresent"],
                    mainName=i["name"],
                    date=dateTime,
                )

                temp.Class.add(_class)
                temp.name.add(_student)
                temp.save()

        return JsonResponse({"status": 200})

    def post(self, request, *args, **kwargs):
        lectureHall = kwargs["lh"]
        classTime = kwargs["classTime"]
        print("kwargs", kwargs)
        data = request.data

        period = kwargs["course"]
        data1 = [
            {
                "name": "Kalandhar Naina Mohammed S",
                "class": "2 CSE - B",
                "rollNumber": "22CS060",
                "isPresent": True,
                "isOD": False,
            },
            {
                "name": "Kishore V",
                "class": "2 CSE - B",
                "rollNumber": "22CS070",
                "isPresent": False,
                "isOD": False,
            },
            {
                "name": "Madhan G",
                "class": "2 CSE - B",
                "rollNumber": "22CS076",
                "isPresent": False,
                "isOD": False,
            },
            {
                "name": "Naveen N",
                "class": "2 CSE - B",
                "rollNumber": "22CS095",
                "isPresent": True,
                "isOD": False,
            },
            {
                "name": "Rahulnisanth M",
                "class": "2 CSE - B",
                "rollNumber": "22CS114",
                "isPresent": True,
                "isOD": False,
            },
            {
                "name": "Ranjith S",
                "class": "2 CSE - B",
                "rollNumber": "22CS118",
                "isPresent": True,
                "isOD": False,
            },
        ]

        _cell = get_period_cell(data[0]["class"], classTime)
        print("cell", _cell)
        dateTime = datetime.now().date()

        for i in data:
            _class = LectureHall.objects.get(className=i["class"])

            _student = Student.objects.get(name=i["name"])

            if i["isPresent"]:
                i["isPresent"] = period.upper() + ":PRESENT"
            elif i["isOD"]:
                i["isPresent"] = period.upper() + ":OD"
            else:
                i["isPresent"] = period.upper() + ":ABSENT"

            stud = LectureHallAttadence.objects.filter(name=_student, date=dateTime)
            # print("_cell[0].Type", type(_cell[0]), _cell[0])
            if list(stud) != []:
                # print(set_cell(i["isPresent"], _cell[0], list(stud)), get_cell_data(_cell[0], set_cell(i["isPresent"], _cell[0], list(stud))))
                set_cell(i["isPresent"], _cell[0], list(stud))
            else:
                temp = LectureHallAttadence.objects.create(
                    mainName=i["name"],
                    date=dateTime,
                )

                temp = set_cell(i["isPresent"], _cell[0], [temp])

                temp.Class.add(_class)
                temp.name.add(_student)
                temp.save()

        return JsonResponse({"status": 200})


class InsertAttendance(APIView):
    def get(self, request, *args, **kwargs):
        status = db.insert_attendance()

        return JsonResponse(
            {
                "status": status,
            }
        )


class getAttendance(APIView):
    def get(self, request, *args, **kwargs):
        # print("kwargs", list(kwargs))
        roll_number = kwargs["rollnumber"]
        sem = kwargs["sem"]
        # _class = lh.split()
        # classes = {"I": 1, "II": 2, "III": 3, "IV": 4, "1": 1, "2": 2, "3": 3, "4": 4}

        # lh = f"{str(classes[_class[0]])} " + " - ".join(_class[1:])

        # attendanceData = {"OOPS": 90, "ADSA": 90, "DBMS": 90, "DM": 90, "Verbal": 90}

        # attendanceData = get_subject_attendance(sem, roll_number)

        # print(sem, roll_number)

        attendanceData = db.get_attendance(sem, roll_number)

        print(list(attendanceData))

        return Response(
            {
                "status": 200,
                "name": roll_number,
                "data": attendanceData,
            }
        )
