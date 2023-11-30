from django.urls import path
from .views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('staff/login/', StaffLoginAPIView.as_view()),
    path('staff/token/refresh/', RefreshAccessToken.as_view(), name='token_obtain_pair'),
    path('admin/login/', AdminLoginAPIView.as_view()),
    path('student/login/', StudentLoginAPIView.as_view()),

]
