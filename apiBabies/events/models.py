from django.db import models

# Create your models here.

class Event(models.Model):
    eventId = models.CharField(max_length=300, primary_key=True)
    eventType = models.CharField(max_length=200)
    eventNotes = models.CharField(max_length=200)
    eventDate = models.DateTimeField()
    babyId = models.ForeignKey(
        'babies.Baby',
        on_delete = models.SET_NULL,
        null = True,
        blank = True
    )
    def __str__(self):
        return self.eventType