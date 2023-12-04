from django.urls import path
from .views import *

urlpatterns = [
    path('', getStudents.as_view()),
]
