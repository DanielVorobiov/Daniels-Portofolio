from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'Home.html')


def login(request):
    return render(request, "Login.html")


def signup(request):
    return render(request,"SignUp.html")