from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Trainer)
admin.site.register(Client)
admin.site.register(Tag)
admin.site.register(UserProfile)
admin.site.register(TrainerSchedule)