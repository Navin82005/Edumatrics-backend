from django.urls import path
from .views import *

urlpatterns = [
    path('<str:dateTime>', GetStudents.as_view()),
    path('mark/<str:lh>/<str:classTime>/<str:course>/', markAttendance.as_view()),
    path('percentage/<str:lh>/<str:student>/', getAttendance.as_view()),
]
