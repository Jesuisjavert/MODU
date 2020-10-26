from accounts.models import Gym
from rest_framework import generics
from ..serializers import GymSerializer

class GymView(generics.ListCreateAPIView):
    queryset = Gym.objects.all()
    serializer_class = GymSerializer