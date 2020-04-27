from django.db import models
from datetime import datetime

# Create your models here.

class Event(models.Model):
    eventType = models.CharField(max_length=200)
    eventNotes = models.CharField(max_length=200)
    eventDate = models.DateTimeField(default=datetime.now())
    babyId = models.ForeignKey(
        'babies.Baby',
        on_delete = models.SET_NULL,
        null = True,
        blank = True
    )
    def __str__(self):
        return self.eventType