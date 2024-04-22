from django.urls import path
from .views import UpdateTimeTable

urlpatterns = [
    # path("update/<str:department>", UpdateTimeTable.as_view(),name="update_timetable"),
    path("update/<str:department>", UpdateTimeTable, name="update_timetable"),
]
