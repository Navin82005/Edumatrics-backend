from django.urls import path
from .views import Dashboard, admin_login, logout_account, verify_admin, InternalStudents

urlpatterns = [
    path("dashboard", Dashboard, name="admin_dashboard"),
    path("student/get/<str:department>", InternalStudents.as_view(), name="admin_dashboard"),
    path("adminlogin", admin_login, name="adminlogin"),
    path("logout", logout_account, name="logout"),
    path("verify/admin/<str:username>", verify_admin, name="verify_admin"),
]
