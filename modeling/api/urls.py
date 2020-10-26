from django.urls import path
from . import views

urlpatterns = [
    path('tag/', views.TagView.as_view(), name="tag"),
    
]