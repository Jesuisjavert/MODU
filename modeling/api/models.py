from django.db import models
from accounts.models import Trainer, Client, Tag
import uuid
# Create your models here.

def program_image_path(instance,filename):
    uuidstr = str(uuid.uuid1())
    total = uuidstr+filename
    return 'api/program/thumb/{0}'.format(total)

class Program(models.Model):
    # 프로그램
    _type = models.CharField(max_length=20)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE, related_name="program")
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=800)
    visit_count = models.IntegerField(default=0)
    tags = models.ManyToManyField(Tag)
    thumb_img = models.ImageField(upload_to=program_image_path)

class ProgramPrice(models.Model):
    # 프로그램 가격 테이블
    program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name="programprice")
    title = models.CharField(max_length=50)
    online_count = models.IntegerField()
    offline_count = models.IntegerField()
    price = models.IntegerField()

class TrainerComment(models.Model):
    # 트레이너 댓글
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE, related_name="trainercomment")
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="trainercomment")
    rate = models.IntegerField()
    content = models.CharField(max_length=800)

class ProgramComment(models.Model):
    # 프로그램 댓글
    program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name="programcomment")
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE, related_name="programcomment")
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="programcomment")
    rate = models.IntegerField()
    content = models.CharField(max_length=800)

class ProgramPayment(models.Model):
    # 결제 완료 테이블
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="programpayment")
    program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name="programpayment")
    price = models.ForeignKey(ProgramPrice, on_delete=models.CASCADE, related_name="programpayment")
    created_at = models.DateTimeField(auto_now_add=True)

class ProgramReservationDay(models.Model):
    # 오프라인 프로그램 예약 날짜 테이블
    program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name="programreservationday")
    day = models.DateField(verbose_name="날짜")

class ProgramReservationTime(models.Model):
    # 오프라인 프로그램 예약날짜에 대한 상세시간 테이블
    ProgramDay = models.ForeignKey(ProgramReservationDay, on_delete=models.CASCADE, related_name="programreservationtime")
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="programreservationtime")
    start_hour = models.DateTimeField()
    end_hour = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class ProgramSchedule(models.Model):
    # 온라인 프로그램 스케줄 테이블
    program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name="progamschedule")
    day = models.CharField(max_length=20, verbose_name="00요일")
    start_hour = models.TimeField()
    end_hour = models.TimeField()

class ProgramRecord(models.Model):
    # 회원의 프로그램을 들은 출석 및 기록(프로그램 활성화 비활성 등등)테이블
    program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name="programrecord")
    programprice = models.ForeignKey(ProgramPrice, on_delete=models.CASCADE, related_name="programrecord")
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="programrecord")
    is_active = models.BooleanField(default=False)
    max_online_count = models.IntegerField()
    max_offline_count = models.IntegerField()
    now_online_count = models.IntegerField(default=0)
    now_offline_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

class ProgramRecordDetail(models.Model):
    # 프로그램 기록 하루 데이터(상세 테이블) 테이블
    programRecord = models.ForeignKey(ProgramRecord, on_delete=models.CASCADE, related_name="programrecorddetail")
    _type = models.CharField(max_length=20)
    content = models.CharField(max_length=800)
    created_at = models.DateTimeField(auto_now_add=True)