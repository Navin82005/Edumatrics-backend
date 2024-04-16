from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse


class InternalMark(APIView):
    def post(self, request, *args, **kwargs):

        return JsonResponse(
            {"data": []},
            status=200,
        )
