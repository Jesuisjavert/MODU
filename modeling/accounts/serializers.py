from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Trainer, Client, UserProfile, Tag, TrainerSchedule
from django.db.models import Avg
User = get_user_model()

class TrainerScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainerSchedule
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class UserProfileSerializer(serializers.ModelSerializer):
    image_url =  serializers.SerializerMethodField(read_only=True)

    def get_image_url(self,userprofile):
        userimage = str(userprofile.profile_img)
        return 'http://d3v9ilm5vhs4go.cloudfront.net/media/'+userimage

    class Meta:
        model = UserProfile
        exclude = ('user',)

class UserSerializers(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField(read_only=True)

    def get_image_url(self,user):
        try:
            userimage = str(user.userprofile.first().profile_img)
            return 'http://d3v9ilm5vhs4go.cloudfront.net/media/'+userimage
        except:
            return 'https://lh3.googleusercontent.com/proxy/sEx-Zh7LpdFg6X1_WLCsb4hIrpfLkIYu_e134TQ-dj0k7MfYNl133Up6r13sCqXJV_8QTVDdx9N2Rh0CM2V4jVydbgTMKmrI80qHKYlQqPzVjHe-YroS6pPoib9Ov2P25jVn0CrVPb3HJ6MJkj1HEX_4RUTBeWCedPw4FtsQ5A'
    class Meta:
        model = User
        fields = ['id','username','is_first','image_url']

class TrainerSerializer(serializers.ModelSerializer):
    user = UserSerializers(read_only=True)
    tags = TagSerializer(read_only=True,many=True)
    trainerschedule = TrainerScheduleSerializer(read_only=True, many=True)
    comment = serializers.SerializerMethodField(read_only=True)

    def get_comment(self,trainer):
        return {
            "count": trainer.trainercomment.count(),
            "rate": trainer.trainercomment.aggregate(Avg('rate'))['rate__avg']
        }

    class Meta:
        model = Trainer
        fields = '__all__'

class ClientSerializer(serializers.ModelSerializer):
    user = UserSerializers(read_only=True)
    tags = TagSerializer(read_only=True,many=True)
    class Meta:
        model = Client
        fields = '__all__'

