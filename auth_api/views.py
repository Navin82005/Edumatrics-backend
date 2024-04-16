from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import (
    StaffLoginSerializer,
    get_tokens_for_user,
    StudentLoginSerializer,
    get_username_from_access_token,
    user_data,
)
from django.contrib.auth import authenticate
from .models import *

# ACCESS TOKEN REFRESHER API
class RefreshAccessToken(APIView):
    def post(self, request, *args, **kwargs):
        refresh_token = request.data["refresh_token"]

        return Response(
            {
                "message": "Token obtained successfully",
                "access_token": refresh_token.access_token,
            },
            status=status.HTTP_200_OK,
        )

class UserDataAPIView(APIView):
    def get(self, request, *args, **kwargs):
        access = request.headers.get("Authorization").split()[1]

        if access is not None:
            user = get_username_from_access_token(access)
            
            if user is not None:
                try:
                    profile = user.profile
                    if profile is not None:
                        _user_data = user_data(user, profile.type)
                        return Response(
                            _user_data,
                            status=status.HTTP_200_OK,
                        )
                    else:
                        new_profile = Profile.objects.create(username=user, type="student")
                        new_profile.save()
                except Exception as e:
                    print("Error auth_api.views.UserDataAPIView: " + str(e))
            else:
                return Response(
                    {"message": "Invalid credentials"},
                    status=status.HTTP_401_UNAUTHORIZED,
                )
        else:
            return Response(
                {"message": "Invalid credentials"},
                status=status.HTTP_401_UNAUTHORIZED,
            )
        return Response(
                {"message": "Invalid credentials"},
                status=status.HTTP_401_UNAUTHORIZED,
            )