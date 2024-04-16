from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.http import JsonResponse, HttpResponseNotFound
from django.contrib.auth.models import User

from .models import Admins
from .serializer import getStudents

from rest_framework.views import APIView
from rest_framework.response import Response

import json


@login_required(login_url="/admin/adminlogin")
def Dashboard(request, *args, **kwargs):
    if request.user.is_authenticated:
        return render(request, "dashboard.html")
    else:
        return redirect("adminlogin")


def admin_login(request):
    if request.method == "POST":
        email_username = request.POST["email"]
        password = request.POST["password"]
        print(request.POST)
        user = authenticate(username=email_username, password=password)
        print("user", user)
        if user != None:
            login(request, user)
            print(request.user.is_authenticated)
            return redirect("admin_dashboard")
        else:
            return render(
                request,
                "adminlogin.html",
                {"error": {"message": "Invalid email or password"}},
            )

    print(request.user.is_authenticated)

    if request.user.is_authenticated:
        return redirect("admin_dashboard")

    return render(
        request,
        "adminlogin.html",
    )


# def verify_admin(request, username):

#     try:
#         user = User.objects.get(username=request.user)
#         print("user.is_authenticated", user.is_authenticated)
#         return JsonResponse({"userStatus": user.is_authenticated}, status=200)
#     except:
#         return JsonResponse({"userStatus": False}, status=404)


def verify_admin(request, username):
    try:
        user = User.objects.get(username=username)
        user_status = user.is_authenticated
        return JsonResponse({"userStatus": user_status}, status=200)
    except User.DoesNotExist:
        return JsonResponse({"error": "User not found"}, status=404)


def logout_account(request):
    logout(request)
    return redirect("/")


class InternalStudents(APIView):
    def get(self, request, *args, **kwargs):
        department = kwargs["department"]
        print(list(kwargs))
        print(list(args))
        sem = request.query_params.get("sem")
        iit = request.query_params.get("iit")
        print(sem, iit)

        data = getStudents(department, sem, iit)
        # data = [
        #     {
        #         "regNo": 714022104095,
        #         "rollNo": "22CS095",
        #         "name": "naveen n",
        #     },
        #     {
        #         "regNo": 714022104096,
        #         "rollNo": "22CS096",
        #         "name": "naveen raj p",
        #     },
        # ]
        # print(data)

        # data_json = json.dumps(data)
        # data_dict = json.loads(data_json)

        return JsonResponse({"students": data}, status=200)
