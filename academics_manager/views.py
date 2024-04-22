from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse
from utils import db
import openpyxl
from .serializers import timetable_extractor

# class UpdateTimeTable(APIView):
#     def get(self, request, *args, **kwargs):
#         status = []
#         if _file := request.FILES.get("dataFille"):
#             file = openpyxl.open(_file, data_only=True)
#             sheet = file.active

#             for row in sheet.iter_rows(values_only=True):
#                 print(list(row))

#             filedata = []

#             db.update_timetable(filedata)

#             return JsonResponse(
#                 {"status": status},
#             )
#         else:
#             return render(request, 'index.html',)


def UpdateTimeTable(request, department):
    status = []
    if request.method == "POST":
        print("request.FILES.get('dataFille')", request.FILES.get("datafile"))
        if _file := request.FILES.get("datafile"):
            file = openpyxl.open(
                _file,
            )

            filedata = timetable_extractor(file)

            timetable = filedata[0]
            
            subjects = filedata[1]
            
            status = [db.update_timetable(timetable)]
            status += [db.update_subjects(subjects)]
            return JsonResponse(
                {"status": status},
            )
        else:
            return JsonResponse(
                {"status": "failed"},
            )
    else:
        return render(
            request,
            "timeTableForm.html",
        )
