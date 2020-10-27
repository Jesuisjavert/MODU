from django.shortcuts import render
from allauth.socialaccount.providers.kakao.views import KakaoOAuth2Adapter
from dj_rest_auth.registration.views import SocialLoginView
from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from .models import User
from rest_framework import generics 
from rest_framework.response import Response
# Create your views here.

class KakaoLogin(SocialLoginView):
    adapter_class = KakaoOAuth2Adapter

class UserInfo(APIView):
    permission_classes = [IsAuthenticated]

    # is_frist 0:초기 1:트레이너 2:클라이언트
    def get_object(self):
        try:
            return User.objects.get(username=self.request.user)
        except:
            return Http404

    def put_user(self, is_first):
        user = self.get_object()
        user.is_first = is_first
        user.save()

    def get(self, request):
        user = self.get_object()
        if user.is_first==1:
            print('트레이너')
            serializer = TrainerSerializer(user)
        elif user.is_first==2:
            print('클라이언트')
            serializer = ClientSerializer(user)
        else:
            print('초기유저')
            serializer = UserSerializers(user)
        return Response(serializer.data)

    def post(self, request, format=None):
        if request.data['is_frist']=='1':
            self.put_user(1)
        else:
            self.put_user(2)
        return Response({"data": True})
