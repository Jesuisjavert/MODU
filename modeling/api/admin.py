from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(TrainerComment)
admin.site.register(Program)
admin.site.register(ProgramComment)
admin.site.register(ProgramPrice)
admin.site.register(ProgramPayment)
admin.site.register(ProgramWebRtc)
admin.site.register(Notification)
admin.site.register(ProgramSchedule)
admin.site.register(ProgramReservationDay)
admin.site.register(ProgramReservationTime)
admin.site.register(ProgramRecord)
admin.site.register(ProgramRecordDetail)
admin.site.register(ChatLog)