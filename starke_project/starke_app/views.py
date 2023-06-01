from django.shortcuts import render, redirect

from django.contrib import messages

from .models import *



def inicio (request):
    return render(request,'starke_app/index.html')