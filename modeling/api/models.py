from django.db import models
from accounts.models import Trainer, Client, Tag
# Create your models here.

class Program(models.Model):
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE, related_name="program")
    visit_count = models.IntegerField(default=0)
    tags = models.ManyToManyField(Tag)
    # create_at = models.DateTimeField(auto_now_add=True,verbose_name='프로그램 등록일')
    # start_date = models.DateField(verbose_name='프로그램 시작일')
    # end_date = models.DateField(verbose_name='프로그램 종료일')
    # class_registration_start_day = models.DateTimeField(verbose_name='프로그램 수강신청 시작날짜')
    # class_registration_end_day = models.DateTimeField(verbose_name='프로그램 수강신청 종료날짜')
    # max_student = models.IntegerField()

class ProgramPrice(models.Model):
    program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name="programprice")
    title = models.CharField(max_length=50)
    online_count = models.IntegerField()
    offline_count = models.IntegerField()
    price = models.IntegerField()

class TrainerComment(models.Model):
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE, related_name="trainercomment")
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="trainercomment")
    rate = models.IntegerField()
    content = models.CharField(max_length=800)

class ProgramComment(models.Model):
    program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name="programcomment")
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
    # is_payment = models.IntegerField(default=0)

class ProgramDayDetail(models.Model):
    Program_detail = models.ForeignKey(ProgramDetail, on_delete=models.CASCADE, related_name="programdaydetail")
    menu = models.CharField(max_length=800)
    chulseok = models.CharField(max_length=100)

class Schedule(models.Model):
    program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name="schedule")
    day = models.CharField(max_length=20)
    start_hour = models.DateTimeField()
    end_hour = models.DatdeTimeField()
    hour = models.IntegerField()