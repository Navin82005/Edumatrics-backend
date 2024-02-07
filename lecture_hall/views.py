from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from attendanceManager.models import StaffTimeTable, LectureHall, LectureHallAttadence
from auth_api.models import Staff, Student

from datetime import datetime
from .serializers import getStudentTimeTable, getStaffTimeTable


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
                    "isActive": True,
                }
                data += [temp]
                # print(str(i.Class.first()), i.course, i.start, i.end)

        print("lecture_hall.views data:", data)

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
        _weekday = datetime.now().weekday()
        # _weekday = 4
        _staff = Staff.objects.get(username=staff_name)
        _times = StaffTimeTable.objects.filter(staffName=_staff, day=weekdays[_weekday])

        data = []

        if list(_times) != []:
            for i in _times:
                isActive = (
                    i.start <= datetime.now().time() and i.end >= datetime.now().time()
                )
                temp = {
                    "class": str(i.Class.first()),
                    "course": i.course,
                    "time": str(i.start)[:-3] + " - " + str(i.end)[:-3],
                    "isActive": isActive,
                }
                data += [temp]

        print(data)

        return Response(
            {
                "Status": 200,
                "Staff": staff_name,
                "timetable": data,
            },
        )


class StaffAllTimeTable(APIView):
    def get(self, request, *args, **kwargs):
        staff_name = kwargs["staff"]
        # {
        #     "monday": [
        #         ["2 CSE - B", "OOPS", "08:30 - 9:30"],
        #         ["2 CSE - B", "OOPS", "10:50 - 11:50"],
        #         ["1 CSE - C", "CTPS", "3:45 - 4:35"],
        #     ],
        #     "tuesday": [
        #         ["2 CSE - B", "OOPS", "08:30 - 9:30"],
        #         ["2 CSE - B", "OOPS", "10:50 - 11:50"],
        #         ["1 CSE - C", "CTPS", "3:45 - 4:35"],
        #     ],
        # }
        data = {
            "monday": [
                ["2 CSE - B", "OOPS", "08:30 - 9:30"],
                ["2 CSE - B", "OOPS", "10:50 - 11:50"],
                ["1 CSE - C", "CTPS", "3:45 - 4:35"],
            ],
            "tuesday": [
                ["2 CSE - B", "OOPS", "08:30 - 9:30"],
                ["2 CSE - B", "OOPS", "10:50 - 11:50"],
                ["1 CSE - C", "CTPS", "3:45 - 4:35"],
            ],
        }
        data = getStaffTimeTable(staff_name)
        return Response(
            {
                "status": 200,
                "data": data,
                "staff": staff_name,
            }
        )


def alterTimeTable(request):
    return render(request, "alterTimeTable.html")


class Student_TimeTable(APIView):
    def post(self, request, *args, **kwargs):
        _class = kwargs["class"]
        data = getStudentTimeTable(_class)

        # print("Data in lecture_hall.views:", data)

        return Response({"status": 200, "class": _class, "data": data})

    def get(self, request, *args, **kwargs):
        _class = kwargs["class"]
        data = getStudentTimeTable(_class)

        # print("Data in lecture_hall.views:", data)

        return Response({"status": 200, "class": _class, "data": data})


class GetClassStudents(APIView):
    def get(self, request, *args, **kwargs):
        lh = kwargs["lh"]
        students = [
            {"name": "Student1", "rollNo": "23cs056"},
            {"name": "Student2", "rollNo": "23cs057"},
            {"name": "Student3", "rollNo": "23cs058"},
        ]
        _class = lh.split()
        classes = {
            "I": 1,
            "II": 2,
            "III": 3,
            "IV": 4,
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
        }
        _class = str(classes[_class[0]]) + " " + " - ".join(_class[1:])

        raw = LectureHall.objects.get(className=_class)
        
        rawList = list(raw.names.all())
        
        
        if rawList != []:
            students = []
            for i in rawList:
                temp = i.get_main_data()
                isActiveList = list(LectureHallAttadence.objects.filter(Class=raw, name=i,date=datetime.now().date()))
                temp["isActive"] = False
                if isActiveList != []:
                    temp = (isActiveList[0].h1).split(":")[1]
                    if temp.lower() == 'present':
                        temp["isActive"] = True
                
                students += [temp]
                
        return Response(
            {
                "status": 200,
                "data": students,
            }
        )


class GetClassStudent(APIView):
    def get(self, request, *args, **kwargs):
        rollNumber = kwargs["rollNumber"]

        data = {}

        if list(Student.objects.filter(rollNumber=rollNumber)) != []:
            user = Student.objects.get(rollNumber=rollNumber)

            data = [user.get_main_data()]

        return Response({"status": 200, "data": data})
