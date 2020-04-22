from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime

# Create your views here.

def welcome(request):
    return HttpResponse("Welcome to the meeting planner")

def date(request):
    return HttpResponse("You have load the page at "+str(datetime.now()))