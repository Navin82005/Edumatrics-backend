from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from rest_framework.views import APIView
from rest_framework.response import Response

class DashBoard(APIView):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return render(request, "dashboard.html")
        else:
            return redirect("adminlogin")

# @login_required(login_url='/admin/adminlogin')
def admin_login(request):
    
    return render(request, "adminlogin.html")
