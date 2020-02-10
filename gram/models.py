from django.db import models
from django.contrib.auth.models import User
import datetime as dt


class Tag(models.Model):
    """ class to indicate the category of the image"""
    name = models.CharField(max_length=30)


class Profile(models.Model):
    profile_photo = models.ImageField(upload_to='profiles/', null=True)
    bio = models.TextField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        '''
        Display for profiles in profile table
        '''
        return self.user.username
