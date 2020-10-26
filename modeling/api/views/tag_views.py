from accounts.models import Tag
from rest_framework import generics
from ..serializers import TagSerializer

class TagView(generics.ListCreateAPIView):
	queryset = Tag.objects.all()
	serializer_class = TagSerializer
