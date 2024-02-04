from django.urls import path
from .views import alterTimeTable, Staff_TimeTable, Student_TimeTable, StaffAllTimeTable

urlpatterns = [
    path('', alterTimeTable),
    path('staff/<str:staff>', Staff_TimeTable.as_view()),
    path('full/staff/<str:staff>', StaffAllTimeTable.as_view()),
    path('student/<str:class>', Student_TimeTable.as_view()),
]
