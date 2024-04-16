from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from django.conf import settings
import jwt

def get_username_from_access_token(access_token):
    try:
        payload = jwt.decode(access_token, settings.SECRET_KEY, algorithms=["HS256"])
        user_id = payload["user_id"]
        user = User.objects.get(id=user_id)
        return user
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None

def user_data(user, type):
    data = {}
    if type == 'student':
        student = user.student
        data["type"] = type
        data["rollNumber"] = student.rollNumber
        data["registerNumber"] = student.registerNumber
        data["name"] = student.name
        data["lectureHall"] = student.lectureHall
        data["inClass"] = student.inClass
        data["userMobile"] = student.userMobile
        data["userDob"] = student.userDob
        data["department"] = student.department
        data["sem"] = student.sem
        return data
    
    return None

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    print(refresh.access_token)

    return {
        "refresh": str(refresh),
        "access": str(refresh.access_token),
    }


class StaffLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class StudentLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
