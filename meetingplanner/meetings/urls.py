from django.urls import path
from meetings.views import detail, list_of_room

urlpatterns = [
    path('<int:id>', detail, name='detail'),
    path('rooms', list_of_room, name='room')
]
