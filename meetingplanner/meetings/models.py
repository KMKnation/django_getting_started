from django.db import models
from datetime import time


class Room(models.Model):
    name = models.CharField(max_length=30)
    floor_num = models.IntegerField()
    room_num = models.IntegerField()

    def __str__(self):
        return str(self.name) + " in " + str(self.room_num) + " room at " + str(self.floor_num) + " floor"

# Create your models here.
class Meeting(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    start_time = models.TimeField(default=time(9))
    duration = models.IntegerField(default=1)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.title) + " at " + str(self.date)

