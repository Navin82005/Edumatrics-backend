from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import LectureHall
from django.http import JsonResponse
import json


# Create your views here.
class getStudents(APIView):
    def post(self, request, *args, **kwargs):
        lectureHall = request.POST["lh"]
        print(lectureHall)
        if LectureHall.objects.filter(className=lectureHall) != None:
            hallData = LectureHall.objects.get(className=lectureHall)
            rawData = hallData.names.all()

            data = {(x.name, x.rollNumber, False) for x in rawData}
            data = sorted(data)
            data = json.dumps(data)
            print(data)
            return JsonResponse(
                {
                    "body": data,
                    # status.HTTP_200_OK,
                }
            )
        else:
            return Response(
                {
                    "Status": "Failed",
                },
            )
