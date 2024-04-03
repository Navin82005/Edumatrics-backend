from django.urls import path
from .views import DashBoard, admin_login

urlpatterns = [
    path("dashboard", DashBoard.as_view(), name="admin_dashboard"),
    path("adminlogin", admin_login, name="adminlogin")
]
