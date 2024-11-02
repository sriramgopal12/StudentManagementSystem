from django.shortcuts import render
from django. urls import path, include
from . import views
# Create your views here.
def StudentHomePage(request):
    return render(request,'studentapp/StudentHomePage.html')

