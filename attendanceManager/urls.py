from django.urls import path
from .views import *

urlpatterns = [
    path('<str:dateTime>', GetStudents.as_view()),
    path('mark/<str:lh>/<str:course>/', markAttendance.as_view()),
]
