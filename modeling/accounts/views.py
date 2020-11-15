from django.shortcuts import render, get_object_or_404
from allauth.socialaccount.providers.kakao.views import KakaoOAuth2Adapter
from dj_rest_auth.registration.views import SocialLoginView
from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from .models import User,TrainerSchedule,Tag
from rest_framework import generics 
from rest_framework.response import Response
from django.http import Http404
# Create your views here.

class KakaoLogin(SocialLoginView):
    #카카오 로그인
    adapter_class = KakaoOAuth2Adapter

class UserInfo(APIView):
    permission_classes = [IsAuthenticated]

    # is_first 0:초기 1:트레이너 2:클라이언트
    def get_object(self):
        try:
            return User.objects.get(username=self.request.user)
        except User.DoesNotExist:
            raise Http404

    def put_user(self, is_first):
        user = self.get_object()
        user.is_first = is_first
        user.save()
        
    # 유저 정보 표기
    def get(self, request):
        user = self.get_object()
        if user.is_first==1:
            serializer = TrainerSerializer(user.trainer.first())
        elif user.is_first==2:
            serializer = ClientSerializer(user.client.first())
        else:
            serializer = UserSerializers(user)
        return Response(serializer.data)

    # 유저 회원가입
    def post(self, request, format=None):
        if request.user.is_first!=0:
            return Response({"message": "이미 회원가입을 하였습니다."}, status=status.HTTP_400_BAD_REQUEST)
        if request.data['is_first']=='1':
            serializer = TrainerSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                trainer = serializer.save(user=request.user)
                self.put_user(1)
                tags = request.data['taglist'].split(',')
                for eachtag in tags:
                    if trainer.tags.filter(name=eachtag).exists():
                        trainer.tags.add(Tag.objects.get(name=eachtag))
                    else:
                        createTag = Tag.objects.create(name=eachtag)
                        trainer.tags.add(createTag)      
                for schedule in request.data['schedule']:
                    if schedule['disabled'] == False:
                        TrainerSchedule.objects.create(day=schedule['day'],start_hour=schedule['start_hour'],end_hour=schedule['end_hour'],trainer=trainer)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer = ClientSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(user=request.user)
                self.put_user(2)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data)
    def put(self,request):
        if request.data['is_first'] == '1':
            logintrainer = request.user.trainer.first()
            serializer = TrainerSerializer(logintrainer,data=request.data)
            if serializer.is_valid(raise_exception=True):
                trainer = serializer.save(user=request.user)
                self.put_user(1)
                origin_tags = trainer.tags.all()
                for origin_tag in origin_tags:
                    trainer.tags.remove(origin_tag)
                tags = request.data['taglist'].split(',')
                for eachtag in tags:
                    if trainer.tags.filter(name=eachtag).exists():
                        trainer.tags.add(Tag.objects.get(name=eachtag))
                    else:
                        createTag = Tag.objects.create(name=eachtag)
                        trainer.tags.add(createTag)    
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.data['is_first'] == '2':
            loginclient = request.user.client.first()
            serializer = ClientSerializer(loginclient,data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(user=request.user)
                self.put_user(2)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data)

class Profile(APIView):
    # 유저 profile 받아오기
    def get(self,request):
        user = User.objects.get(id=request.user.id)
        if user.userprofile.all().exists():
            userprofile = user.userprofile.all().first()
            serializers = UserProfileSerializer(userprofile)
            return Response(serializers.data)
        else:
            return Response({'data':False})

    # 유저 profile 업로드
    def post(self,request):
        loginuser = User.objects.get(id=request.user.id)
        if loginuser.userprofile.all().exists():
            loginuser.userprofile.all().delete()
        serializers = UserProfileSerializer(data=request.data)
        if serializers.is_valid(raise_exception=True):
            serializers.save(user=request.user)
            return Response(serializers.data)
        return Response(serializers.data)
