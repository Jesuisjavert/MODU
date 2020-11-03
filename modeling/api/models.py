from django.db import models
from accounts.models import Trainer, Client, Tag
# Create your models here.

class Program(models.Model):
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE, related_name="program")
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=800)
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

class ProgramDay(models.Model):
    program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name="programday")
    day = models.DateField()

class ProgramDayTime(models.Model):
    ProgramDay = models.ForeignKey(ProgramDay, on_delete=models.CASCADE, related_name="programdaytime")
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="programdaytime")
    start_hour = models.DateTimeField()
    end_hour = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Schedule(models.Model):
    program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name="schedule")
    day = models.CharField(max_length=20)
    start_hour = models.DateTimeField()
    end_hour = models.DateTimeField()

class ProgramHoliday(models.Model):
    program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name="programholiday")
    # program 휴일 (일자, 휴일내용)
    day = models.DateField()
    content = models.CharField(max_length=100)

class ProgramRecord(models.Model):
    program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name="programrecord")
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="programrecord")
    max_online_count = models.IntegerField()
    max_offline_count = models.IntegerField()
    now_online_count = models.IntegerField()
    now_offline_count = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

class ProgramRecordDetail(models.Model):
    programRecord = models.ForeignKey(ProgramRecord, on_delete=models.CASCADE, related_name="programrecorddetail")
    type = models.CharField(max_length=10)
    content = models.CharField(max_length=800)