from django.db import models
from accounts.models import Trainer, Client, Tag
# Create your models here.

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

class ProgramPayment(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="programpayment")
    program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name="programpayment")

class ProgramDetail(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="programdetail")
    program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name="programdetail")

class ProgramDayDetail(models.Model):
    Program_detail = models.ForeignKey(ProgramDetail, on_delete=models.CASCADE, related_name="programdaydetail")
    menu = models.CharField(max_length=800)
    chulseok = models.CharField(max_length=100)

class Schedule(models.Model):
    program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name="schedule")
    day = models.CharField(max_length=20)
    start_hour = models.DateTimeField()
    end_hour = models.DateTimeField()
    hour = models.IntegerField()