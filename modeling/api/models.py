from django.db import models
from accounts.models import Trainer, Client
# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=100)

class Program(models.Model):
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE, related_name="program")
    price = models.IntegerField()
    visit_count = models.IntegerField(default=0)
    tags = models.ManyToManyField(Tag)

class TrainerComment(models.Model):
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE, related_name="trainercomment")
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="trainercomment")
    rate = models.IntegerField()
    content = models.CharField(max_length=800)

class ProgramComment(models.Model):
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE, related_name="programcomment")
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="programcomment")
    rate = models.IntegerField()
    content = models.CharField(max_length=800)