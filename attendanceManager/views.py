from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import LectureHall, LectureHallAttadence
from django.http import JsonResponse
import json
from datetime import datetime
from auth_api.models import Student
from .serializers import get_period_cell, set_cell, get_cell_data


# Create your views here.
class GetStudents(APIView):
    def post(self, request, *args, **kwargs):
        lectureHall = request.POST["lh"]
        _now_time = kwargs['dateTime']
        print(lectureHall)
        if LectureHall.objects.filter(className=lectureHall) != None:
            hallData = LectureHall.objects.get(className=lectureHall)
            rawData = hallData.names.all()

            _period = get_period_cell(lectureHall)[1]

            # data = [{"name" : x.name, x.rollNumber, False} for x in rawData]
            data = []

            # rawData = sorted(rawData)
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
                temp = LectureHallAttadence.objects.filter(mainName=i['name'], date=date)
                if list(temp) != []:
                    # print(i["name"], temp[0])
                    print(get_period_cell(lectureHall)[0])
                    cell_data = get_cell_data(cell=get_period_cell(lectureHall, _now_time=_now_time)[0], instance=temp[0])
                    if cell_data != None:
                        i["isPresent"] = cell_data["present"]
                        i["isOD"] = cell_data["od"]

            # Sorted_dict = sorted(data, key=lambda x: x["name"])
            # data = Sorted_dict
            # print(data)
            # data = json.dumps(Sorted_dict)
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
                print(stud)
                set_cell(i["isPresent"], _cell, list(stud))

            else:
                temp = LectureHallAttadence.objects.create(
                    h1=i["isPresent"],
                    mainName=i["name"],
                    date=dateTime,
                )
                # set_cell(i["isPresent"], _cell, stud)

                temp.Class.add(_class)
                temp.name.add(_student)
                temp.save()

        return JsonResponse({"status": 200})

    def post(self, request, *args, **kwargs):
        lectureHall = kwargs["lh"]
        data = request.data
        # print(lectureHall)
        # lectureHall = kwargs["lh"]

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
                print(stud)
                set_cell(i["isPresent"], _cell[0], list(stud))

            else:
                temp = LectureHallAttadence.objects.create(
                    mainName=i["name"],
                    date=dateTime,
                )
                # set_cell(i["isPresent"], _cell[0], stud)
                
                temp = set_cell(i["isPresent"], _cell[0], [temp])

                temp.Class.add(_class)
                temp.name.add(_student)
                temp.save()

        return JsonResponse({"status": 200})
