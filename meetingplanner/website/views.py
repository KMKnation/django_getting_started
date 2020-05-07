from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime

# Create your views here.

def welcome(request):
    return render(request, 'website/welcome.html',
                  {"message": "This line comes from python views by passing context !!"})

def date(request):
    return HttpResponse("You have load the page at "+str(datetime.now()))