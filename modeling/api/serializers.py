from rest_framework import serializers
from .models import *
from accounts.models import Gym
from accounts.serializers import ClientSerializer

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class GymSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gym
        fields = '__all__'

class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainer
        fields = '__all__'

class TrainerCommentSerialiezr(serializers.ModelSerializer):
    client = ClientSerializer(read_only=True)
    class Meta:
        model = TrainerComment
        fields = ('id','rate', 'content','client')