from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    print(refresh.access_token)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

class StaffLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
