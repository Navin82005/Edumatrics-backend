from django.urls import path
from .views import *

urlpatterns = [
    path('', getStudents.as_view()),
    path('mark/<str:lh>/', markAttendance.as_view()),
]
