from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

                  
class UserProfile(models.Model):
    username = models.CharField(max_length=100, unique=True, null=True)
    password = models.CharField(max_length=100, null=True)
    email = models.EmailField(unique=True, null=True)
    name = models.CharField(max_length=100, null=True)
    phone_number = models.CharField(max_length=15, null=True)
    # Add other fields as needed

    def __str__(self):
        return self.username


# Create your models here.
class profile_details(models.Model):
    fname = models.CharField(max_length=20 ,default="")
    uname = models.CharField(max_length=20 ,default="")
    email = models.CharField(max_length=30 ,default="")
    phone = models.IntegerField(default="")
    address1 = models.CharField(max_length=20 ,default="")
    address2 = models.CharField(max_length=20 ,default="")
    state = models.CharField(max_length=20 ,default="")
    country = models.CharField(max_length=20 ,default="")