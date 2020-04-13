from pyexpat.errors import messages

from django.shortcuts import render, redirect
from rest_framework.response import Response

from .serializers import *
from django.contrib.auth.models import User
from django.contrib.auth import logout as django_logout

from rest_framework import viewsets, status
# Create your views here.


from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
def login(request):
    return render(request, "login.html")


@login_required
def home(request):
    return render(request, 'home.html')


def register(request):
    return render(request,'register.html')

# @api_view()
def savedetails(request):
    try:
        n=request.POST["name"]
        e=request.POST["email"]
        p=request.POST["password"]
        User(username=n,email=e,password=p).save()
        messages.success(request,"registered Successfully, Please Login To access Dashboard")
        return redirect("main")
    except:
        messages.success(request, "Email Already Exstised Please login")
        return redirect("main")

def verityuser(request):
    e = request.POST["email"]
    p = request.POST["password"]
    try:
        res=User.objects.get(email=e,password=p)
    except User.DoesNotExist:
        messages.success(request, "Details Not Match Please register")
        return redirect("main")
    else:
        request.session["email"] = e
        return redirect("welcome")