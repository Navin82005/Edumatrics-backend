from django.urls import path
from .views import InsertAttendance, getAttendance, MarkAttendance

urlpatterns = [
    # path('<str:dateTime>', GetStudents.as_view()),
    # path('mark/<str:lh>/<str:classTime>/<str:course>/', markAttendance.as_view()),
    # 
    # TO insert new attendances or update
    path("commercial/update/", InsertAttendance.as_view()),
    # 
    # TO get the respective attendance of a student
    path("get/<str:sem>/<str:rollnumber>", getAttendance.as_view()),
    # 
    # To mark attendances
    path("mark/attendance/", MarkAttendance),
]
