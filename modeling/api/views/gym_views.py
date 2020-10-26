from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from accounts.models import Gym
from rest_framework import generics
from rest_framework.views import APIView
from ..serializers import GymSerializer

class GymView(generics.ListCreateAPIView):
    queryset = Gym.objects.all()
    serializer_class = GymSerializer

class GymDetailView(APIView):
    def get_object(self, pk):
        return get_object_or_404(Gym, pk=pk)
      
    def get(self, request, pk, format=None):
        gym = self.get_object(pk)
        serializer = GymSerializer(gym)
        return Response(serializer.data)

    def delete(self, request, pk):
        queryset = self.get_object(pk)
        try:
            queryset.delete()
            return Response(status=status.HTTP_201_CREATED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)