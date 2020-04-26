from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Parent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

@receiver(post_save, sender=User)
def create_user_parent(sender, instance, created, **kwargs):
    if created:
        Parent.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_parent(sender, instance, **kwargs):
    instance.parent.save()