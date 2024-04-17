from django.urls import path
from .views import *

urlpatterns = [
    # path('<str:dateTime>', GetStudents.as_view()),
    # path('mark/<str:lh>/<str:classTime>/<str:course>/', markAttendance.as_view()),
    path('mark', InsertAttendance.as_view()),
    path('percentage/<str:sem>/<str:rollnumber>', getAttendance.as_view()),
]
