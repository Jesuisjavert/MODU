from rest_framework import serializers
from .models import *
from accounts.models import Gym
from accounts.serializers import ClientSerializer, TrainerSerializer

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class GymSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gym
        fields = '__all__'

# class TrainerSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Trainer
#         fields = '__all__'

class TrainerCommentSerializer(serializers.ModelSerializer):
    client = ClientSerializer(read_only=True)
    class Meta:
        model = TrainerComment
        fields = ('id','rate', 'content','client')

class ProgramPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgramPrice
        fields = '__all__'

class ProgramSerialiezer(serializers.ModelSerializer):
    trainer = TrainerSerializer(read_only=True)
    image_url =  serializers.SerializerMethodField(read_only=True)
    programprice = ProgramPriceSerializer(read_only=True, many=True)
    tags = TagSerializer(read_only=True,many=True)
    def get_image_url(self,program):
        image = str(program.thumb_img)
        return 'http://d3v9ilm5vhs4go.cloudfront.net/media/'+image
    class Meta:
        model = Program
        fields = '__all__'

class ProgramCommentSerializer(serializers.ModelSerializer):
    client = ClientSerializer(read_only=True)
    class Meta:
        model = ProgramComment
        exclude = ('program','trainer')

class ProgramUserSerialiezr(serializers.ModelSerializer):
    client = ClientSerializer(read_only=True)
    class Meta:
        model = ProgramPayment
        fields = ('client',)

class ProgramPaymentSerialiezr(serializers.ModelSerializer):
    class Meta:
        model = ProgramPayment
        fields = ()
