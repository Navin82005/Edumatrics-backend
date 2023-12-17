from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from attendanceManager.models import StaffTimeTable
from auth_api.models import Staff
from datetime import datetime

class Staff_TimeTable(APIView):
    def get(self, request, *args, **kwargs):
        staff_name = kwargs["staff"]
        weekdays = {
            0: "monday",
            1: "tuesday",
            2: "wednesday",
            3: "thursday",
            4: "friday",
            5: "saturday",
            6: "sunday",
        }
        # _weekday = datetime.now().weekday()
        _weekday = 4
        _staff = Staff.objects.get(username=staff_name)
        _times = StaffTimeTable.objects.filter(staffName=_staff, day=weekdays[_weekday])

        data = []

        if list(_times) != []:
            for i in _times:
                temp = {
                    "class": str(i.Class.first()),
                    "course": i.course,
                    "time": str(i.start)[:-3] + "-" + str(i.end)[:-3],
                }
                data += [temp]
                # print(str(i.Class.first()), i.course, i.start, i.end)

        print(data)

        return Response(
            {
                "Status": 200,
                "Staff": staff_name,
                "timetable": data,
            },
        )

    def post(self, request, *args, **kwargs):
        staff_name = kwargs["staff"]
        weekdays = {
            0: "monday",
            1: "tuesday",
            2: "wednesday",
            3: "thursday",
            4: "friday",
            5: "saturday",
            6: "sunday",
        }
        # _weekday = datetime.now().weekday()
        _weekday = 4
        _staff = Staff.objects.get(username=staff_name)
        _times = StaffTimeTable.objects.filter(staffName=_staff, day=weekdays[_weekday])

        data = []

        if list(_times) != []:
            for i in _times:
                temp = {
                    "class": str(i.Class.first()),
                    "course": i.course,
                    "time": str(i.start)[:-3] + "-" + str(i.end)[:-3],
                }
                data += [temp]
                # print(str(i.Class.first()), i.course, i.start, i.end)

        print(data)

        return Response(
            {
                "Status": 200,
                "Staff": staff_name,
                "timetable": data,
            },
        )


# Create your views here.
def alterTimeTable(request):
    return render(request, "alterTimeTable.html")
