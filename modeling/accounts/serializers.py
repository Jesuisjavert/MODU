from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Trainer, Client

User = get_user_model()

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','is_first']

class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainer
        exclude = ('user','tags')

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        exclude = ('user','tags')