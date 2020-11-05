from django.urls import path
from . import views

urlpatterns = [
    path('tag/', views.TagView.as_view(), name="tag"),
    path('gym/', views.GymView.as_view(), name="gym"),
    path('gym/<int:pk>/', views.GymDetailView.as_view(), name="gymdetail"),
    path('trainer/', views.TrainerView.as_view(), name="trainer"),
    path('trainer/<int:pk>/', views.TrainerDetailView.as_view(), name="trainerdetail"),
    path('trainer/<int:pk>/comment/', views.TrainerCommentView.as_view(), name="trainercomment"),
    path('trainer/comment/<int:pk>/', views.TrainerCommentDetailView.as_view(), name="trainercommentdetail"),
    path('trainer/program/', views.TrainerProgramView.as_view(), name="trainerprogram"),
    path('program/', views.ProgramView.as_view(), name="program"),
    path('program/<int:pk>/', views.ProgramDetailView.as_view(), name="programdetail"),
    path('program/<int:pk>/user/', views.ProgramUserView.as_view(), name="programuser"),
    path('program/<int:pk>/comment/', views.ProgramCommentView.as_view(), name="programcomment"),
    path('program/comment/<int:pk>/', views.ProgramCommentDetailView.as_view(), name="programcommentdetail"),
    path('kakaopay/', views.KakaoPay.as_view(), name="kakaopay"),
    path('kakaopay/approve/', views.KakaoPayApprove.as_view(), name="kakaopayapprove"),
]