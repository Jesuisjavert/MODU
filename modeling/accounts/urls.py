from django.urls import path
from . import views

urlpatterns = [
    path('kakao/login/', views.KakaoLogin.as_view()),
    path('user/',views.UserInfo.as_view()),
    path('user/profile/',views.Profile.as_view(),name='Profile'),
]