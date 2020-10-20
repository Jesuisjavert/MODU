from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    is_first = models.IntegerField(default=0)


class UserProfile(models.Model):
    # 이미지경로 나중에 추가 필요함
    profile_img = models.ImageField(blank=True,null=True)
