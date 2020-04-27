from django.db import models

# Create your models here.

class Baby(models.Model):
    babyName = models.CharField(max_length=200)
    babyLastname = models.CharField(max_length=200)
    parent = models.ForeignKey(
        'parents.Parent',
        on_delete = models.SET_NULL,
        null = True,
        blank = True
    )

    def __str__(self):
        return str(self.parent.user_id)
