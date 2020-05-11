from django.shortcuts import render, get_object_or_404
from meetings.models import Meeting, Room
from django.forms import modelform_factory

MeetingForm = modelform_factory(Meeting, exclude=[])


# Create your views here.

def detail(request, id):
    meeting = get_object_or_404(Meeting, pk=id)
    return render(request,
                  'meetings/detail.html',
                  {'meeting': meeting})


def list_of_room(request):
    return render(request,
                  'meetings/rooms.html',
                  {'total': Room.objects.count(),
                   'rooms': Room.objects.all()})


def create(request):
    return render(request,
                  'meetings/new.html',
                  context={'form': MeetingForm})
