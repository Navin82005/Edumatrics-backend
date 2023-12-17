from django.urls import path
from .views import alterTimeTable, Staff_TimeTable

urlpatterns = [
    path('', alterTimeTable),
    path('staff/<str:staff>', Staff_TimeTable.as_view()),
]
