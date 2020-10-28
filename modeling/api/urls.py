from django.urls import path
from . import views

urlpatterns = [
    path('tag/', views.TagView.as_view(), name="tag"),
    path('gym/', views.GymView.as_view(), name="gym"),
    path('gym/<int:pk>/', views.GymDetailView.as_view(), name="gymdetail"),
    path('trainer/', views.TrainerView.as_view(), name="trainer"),
    path('trainer/<int:pk>/', views.TrainerDetailView.as_view(), name="trainerdetail"),
    path('trainer/<int:pk>/comment/', views.TrainerCommentView.as_view(), name="trainercomment"),
    path('trainer/comment/<int:pk>/', views.TrainerCommentDetailView.as_view(), name="trainercommentdetail")
]