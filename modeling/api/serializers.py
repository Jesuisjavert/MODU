from rest_framework import serializers
from .models import *
from accounts.models import Gym, TrainerSchedule
from accounts.serializers import ClientSerializer, TrainerSerializer, UserSerializers, TagSerializer

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

class ProgramScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgramSchedule
        fields ='__all__'

class ProgramSerialiezer(serializers.ModelSerializer):
    trainer = TrainerSerializer(read_only=True)
    image_url =  serializers.SerializerMethodField(read_only=True)
    programprice = ProgramPriceSerializer(read_only=True, many=True)
    tags = TagSerializer(read_only=True,many=True)
    programschedule = ProgramScheduleSerializer(read_only=True, many=True)
    def get_image_url(self,program):
        print(program)
        image = str(program.thumb_img)
        return 'http://d3v9ilm5vhs4go.cloudfront.net/media/'+image
    class Meta:
        model = Program
        fields = '__all__'


# onlineProgram을 위한 거
class ProgramOnlieSerialiezer(ProgramSerialiezer):
    programschedule = ProgramScheduleSerializer(read_only=True, many=True)

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
    program = ProgramSerialiezer(read_only=True)
    price = ProgramPriceSerializer(read_only=True)
    class Meta:
        model = ProgramPayment
        fields = ('program', 'price')


# 클라이언트 mypage를 위한 Serializer
class ClientProgramCommentSerializer(serializers.ModelSerializer):
    program = ProgramSerialiezer(read_only=True)
    class Meta:
        model = ProgramComment
        fields = '__all__'

class ClientTrainerCommentSerializer(serializers.ModelSerializer):
    trainer = TrainerSerializer(read_only=True)
    class Meta:
        model = TrainerComment
        fields = '__all__'

class ClientDetailSerializer(serializers.ModelSerializer):
    user = UserSerializers(read_only=True)
    programpayment = ProgramPaymentSerialiezr(read_only=True, many=True)
    trainercomment = ClientTrainerCommentSerializer(read_only=True, many=True)
    programcomment = ClientProgramCommentSerializer(read_only=True, many=True)
    class Meta:
        model = Client
        fields = '__all__'

class ClientNotificationSerializer(serializers.ModelSerializer):
    program_title = serializers.CharField(source='program.title')
    class Meta:
        model = Notification
        fields = '__all__'

class ProgramReservationDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgramReservationDay
        fields = '__all__'

class ProgramReservationTime(serializers.ModelSerializer):
    class Meta:
        model = ProgramReservationTime
        fields = '__all__'

class ChatRoomSerializer(serializers.ModelSerializer):
    client_name = serializers.CharField(source='client.user.username')
    class Meta:
        model = ChatRoom
        fields = '__all__'
class ChatLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatLog
class ProgramRecordSerializer(serializers.ModelSerializer):
    program_title = serializers.CharField(source='program.title')
    program_type = serializers.CharField(source='program._type')
    program_price = serializers.CharField(source='programprice.price')
    program_price_title = serializers.CharField(source='programprice.title')
    image_url = serializers.SerializerMethodField(read_only=True)
    trainer_name = serializers.CharField(source='program.trainer.name')
    def get_image_url(self,programrecord):
        
        image = str(programrecord.program.thumb_img)
        return 'http://d3v9ilm5vhs4go.cloudfront.net/media/'+image
    class Meta:
        model = ProgramRecord
        fields = '__all__'