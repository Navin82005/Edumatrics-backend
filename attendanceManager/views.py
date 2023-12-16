from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import LectureHall, LectureHallAttadence
from django.http import JsonResponse
import json
from datetime import datetime
from auth_api.models import Student
from .serializers import get_period_cell

# Create your views here.
class getStudents(APIView):
    def post(self, request, *args, **kwargs):
        lectureHall = request.POST["lh"]
        print(lectureHall)
        if LectureHall.objects.filter(className=lectureHall) != None:
            hallData = LectureHall.objects.get(className=lectureHall)
            rawData = hallData.names.all()

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

            Sorted_dict = sorted(data, key=lambda x: x["name"])
            data = Sorted_dict
            print(data)
            # data = json.dumps(Sorted_dict)
            return Response(
                {
                    "body": data,
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

        for i in data:
            _class = LectureHall.objects.get(className=i["class"])
            # print(_class)
            _student = Student.objects.get(name=i["name"])

            if i["isPresent"]:
                i["isPresent"] = period.upper() + ":PRESENT"
            else:
                i["isPresent"] = period.upper() + ":ABSENT"

            dateTime = datetime.now().date()



            stud = LectureHallAttadence.objects.filter(
                mainName=i["name"], date=dateTime
            )
            print(stud)
            if (LectureHallAttadence.objects.filter(mainName=i["name"], date=dateTime)) is not None:
                print("cell", get_period_cell(i['class']))
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

    # def post(self, request, *args, **kwargs):
    #     # lectureHall = kwargs["lh"]
    #     # data = request.data
    #     # print(lectureHall)

    #     data = [
    #         {
    #             "name": "KALANDHAR NAINA MOHAMMED S",
    #             "class": "2 CSE - B",
    #             "rollNumber": "22CS060",
    #             "isPresent": True,
    #             "isOD": False,
    #         },
    #         {
    #             "name": "Kishore V",
    #             "class": "2 CSE - B",
    #             "rollNumber": "22CS070",
    #             "isPresent": False,
    #             "isOD": False,
    #         },
    #         {
    #             "name": "Madhan G",
    #             "class": "2 CSE - B",
    #             "rollNumber": "22CS076",
    #             "isPresent": False,
    #             "isOD": False,
    #         },
    #         {
    #             "name": "Naveen",
    #             "class": "2 CSE - B",
    #             "rollNumber": "22CS095",
    #             "isPresent": True,
    #             "isOD": False,
    #         },
    #         {
    #             "name": "Rahulnisanth M",
    #             "class": "2 CSE - B",
    #             "rollNumber": "22CS114",
    #             "isPresent": True,
    #             "isOD": False,
    #         },
    #         {
    #             "name": "Ranjith S",
    #             "class": "2 CSE - B",
    #             "rollNumber": "22CS118",
    #             "isPresent": True,
    #             "isOD": False,
    #         },
    #     ]

    #     for i in data:
    #         temp = LectureHallAttadence.objects.create()
    #         for j in i:
    #             print(j, i[j])

    #     return JsonResponse({"status": 200})
