from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.conf import settings
# Create your models here.

class Skyscraper(models.Model):
    
    
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    discription = models.TextField(default="one of the skyscrapers")
    
    height = models.IntegerField(default=200)
    floors = models.IntegerField(default=50)


    def __str__(self):
        return self.title




