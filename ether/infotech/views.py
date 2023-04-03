from django.shortcuts import render,redirect
from .models import *

# Create your views here.

def home(request):
    return render(request,'index.html')

def course(request):
    return render(request,'Divya.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def cd(request):
    firstname = request.POST["firstname"]
    lastname = request.POST["lastname"]
    email = request.POST["email"]
    message = request.POST["message"]
    mobile = request.POST["mobile"]

    newuser = form.objects.create(
        firstname=firstname,lastname=lastname,email=email,message=message,mobile=mobile)
    return render(request,'cd.html')


def gallery(request):
    return render(request,'Nasir.html')
