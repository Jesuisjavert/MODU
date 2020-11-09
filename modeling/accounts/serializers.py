from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Trainer, Client, UserProfile

User = get_user_model()

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
            return None
    class Meta:
        model = User
        fields = ['id','username','is_first','image_url']

class TrainerSerializer(serializers.ModelSerializer):
    user = UserSerializers(read_only=True)
    class Meta:
        model = Trainer
        exclude = ('tags',)

class ClientSerializer(serializers.ModelSerializer):
    user = UserSerializers(read_only=True)
    class Meta:
        model = Client
        exclude = ('tags',)
