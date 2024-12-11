from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework import Token
# Create your models here.

class User(models.Model):   # created user with field name
    name= models.CharField(max_length=100)

@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):   # created a function that creates auth token
    if created:
        Token.objects(user=instance)

