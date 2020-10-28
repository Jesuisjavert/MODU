from django.urls import path
from . import views

urlpatterns = [
    path('kakao/login/', views.KakaoLogin.as_view()),
    path('user/',views.UserInfo.as_view()),
    path('test/',views.test)
]