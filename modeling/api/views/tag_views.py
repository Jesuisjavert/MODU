from accounts.models import Tag
from rest_framework import generics
from ..serializers import TagSerializer

class TagView(generics.ListCreateAPIView):
	# 태그 정보 GET, POST
	queryset = Tag.objects.all()
	serializer_class = TagSerializer