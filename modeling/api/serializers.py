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

class TrainerCommentSerializer(serializers.ModelSerializer):
    client = ClientSerializer(read_only=True)
    class Meta:
        model = TrainerComment
        fields = ('id','rate', 'content','client')

class ProgramSerialiezer(serializers.ModelSerializer):
    trainer = TrainerSerializer(read_only=True)
    image_url =  serializers.SerializerMethodField(read_only=True)
    def get_image_url(self,program):
        image = str(program.thumb_img)
        return 'http://d3v9ilm5vhs4go.cloudfront.net/media/'+image
    class Meta:
        model = Program
        exclude = ('tags',)

class ProgramCommentSerializer(serializers.ModelSerializer):
    client = ClientSerializer(read_only=True)
    class Meta:
        model = ProgramComment
        exclude = ('program','trainer')