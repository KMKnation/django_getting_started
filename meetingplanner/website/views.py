from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime

from meetings.models import Meeting

# Create your views here.

def welcome(request):
    return render(request, 'website/welcome.html',
                  {"meetings_count": Meeting.objects.count()})

def date(request):
    return HttpResponse("You have load the page at "+str(datetime.now()))