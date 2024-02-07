from django.urls import path
from .views import (
    alterTimeTable,
    Staff_TimeTable,
    Student_TimeTable,
    StaffAllTimeTable,
    GetClassStudents,
    GetClassStudent,
)

urlpatterns = [
    path("", alterTimeTable),
    path("staff/<str:staff>", Staff_TimeTable.as_view()),
    path("full/staff/<str:staff>", StaffAllTimeTable.as_view()),
    path("student/<str:class>", Student_TimeTable.as_view()),
    path("staff/get-class/<str:lh>", GetClassStudents.as_view()),
    path("staff/get-student/<str:rollNumber>", GetClassStudent.as_view()),
]
