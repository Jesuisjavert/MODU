from django.urls import path
from . import views

urlpatterns = [
    path('kakao/login/', views.KakaoLogin.as_view()),
]