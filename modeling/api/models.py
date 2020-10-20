from django.db import models
from accounts.models import Trainer
# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=100)

class Program(models.Model):
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE, related_name="program")
    price = models.IntegerField()
    visit_count = models.IntegerField(default=0)