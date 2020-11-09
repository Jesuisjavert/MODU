from accounts.models import Client
from rest_framework.views import APIView
from ..serializers import ClientDetailSerializer
from rest_framework.response import Response

class ClientView(APIView):
		def get(self, request):
				client = Client.objects.get(pk=request.user.client.first().id)
				serializer = ClientDetailSerializer(client)
				return Response(serializer.data)