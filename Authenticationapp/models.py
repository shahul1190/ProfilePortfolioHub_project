from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User



# Create your models here.
class Profile(models.Model):
    username=models.CharField(max_length=200)
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    email=models.EmailField(max_length=200)
    password=models.CharField(max_length=200)
    password1=models.CharField(max_length=200)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    address = models.CharField(max_length=400)
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    postal_code = models.IntegerField(null=True)
    phone = models.IntegerField(null=True)
    place = models.CharField(max_length=200)
    profile_picture = models.ImageField(upload_to='profile_pictures/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


def __str__(self):
        return '{}'.format(self.username)







