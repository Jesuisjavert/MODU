from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
# Create your models here.

class User(AbstractUser):
    is_first = models.IntegerField(default=0)


class UserProfile(models.Model):
    # 이미지경로 나중에 추가 필요함
    profile_img = models.ImageField(blank=True,null=True)

class Client(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='client')
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)

class Gym(models.Model):
    lat = models.FloatField()
    lon = models.FloatField()
    name = models.CharField(max_length=50)

class Trainer(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='trainer')
    gym = models.ForeignKey(Gym, default=None, on_delete=models.SET_DEFAULT, related_name='trainer', null=True, blank=True)
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    content = models.CharField(max_length=800)
    gender = models.CharField(max_length=10)
    age = models.IntegerField()