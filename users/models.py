from django.db import models
from django.contrib.auth.models import User
import datetime

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.CharField(max_length=100)
    phone = models.IntegerField()
    password =models.CharField(max_length=100, default='',)
    created_date = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return self.name
