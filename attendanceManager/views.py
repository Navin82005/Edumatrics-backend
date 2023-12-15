from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import LectureHall, LectureHallAttadence
from django.http import JsonResponse
import json
from datetime import datetime


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
    def post(self, request, *args, **kwargs):
        lectureHall = kwargs["lh"]
        data = request.data
        print(lectureHall)

        for i in data:
            for j in i:
                print(i[j])

        return JsonResponse({"status": 200})
