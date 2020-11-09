from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
import uuid
# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=100)

class User(AbstractUser):
    is_first = models.IntegerField(default=0)

def user_image_path(instance,filename):
    uuidstr = str(uuid.uuid1())
    total = uuidstr+filename
    return 'api/profile/{0}'.format(total)

class UserProfile(models.Model):
    profile_img = models.ImageField(upload_to=user_image_path, blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='userprofile')


class Client(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='client')
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    tags = models.ManyToManyField(Tag)

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
    tags = models.ManyToManyField(Tag)

class TrainerSchedule(models.Model):
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE, related_name="trainerschedule")
    day = models.CharField(max_length=20, verbose_name="00요일")
    start_hour = models.DateTimeField()
    end_hour = models.DateTimeField()

class TrainerHoliday(models.Model):
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE, related_name="trainerholiday")
    day = models.DateField(verbose_name="날짜")