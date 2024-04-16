from django.urls import path
from .views import StudentAdder

urlpatterns = [
    path('add/students', StudentAdder, name='StudentAdder'),
]