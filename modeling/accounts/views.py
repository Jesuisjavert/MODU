from django.shortcuts import render
from allauth.socialaccount.providers.kakao.views import KakaoOAuth2Adapter
from dj_rest_auth.registration.views import SocialLoginView
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from .models import User
from rest_framework import generics 
from rest_framework.response import Response
# Create your views here.

class KakaoLogin(SocialLoginView):
    adapter_class = KakaoOAuth2Adapter

class UserInfo(generics.ListAPIView):
    queryset = User
    serializer_class = UserSerializers
    permission_classes =[IsAuthenticated]
    def get_object(self):
        try:
            return User.objects.get(username=self.request.user)
        except:
            return Http404
    def get(self,request):
        queryset = self.get_object()
        serializer_class = UserSerializers(queryset)
        return Response(serializer_class.data)