from django.shortcuts import render
from meetings.models import Meeting

# Create your views here.

def detail(request, id):
    return render(request,
                  'meetings/detail.html',
                  {'meeting': Meeting.objects.get(pk=id)})