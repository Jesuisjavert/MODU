from django.urls import path
from . import views

urlpatterns = [
    path('tag/', views.TagView.as_view(), name="tag"),
    path('gym/', views.GymView.as_view(), name="gym"),
    path('gym/<int:pk>/', views.GymDetailView.as_view(), name="gymdetail"),
    path('trainer/<int:pk>/comment/', views.TrainerComment.as_view(), name="trainercomment"),
]