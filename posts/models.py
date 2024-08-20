from django.db import models

from users.models import UserProfile
import datetime

class Post(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=255, blank=False, null=False)
    content = models.TextField()
    created_date = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return self.title
