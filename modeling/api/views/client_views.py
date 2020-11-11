from accounts.models import Client
from rest_framework.views import APIView
from ..serializers import ClientDetailSerializer,ClientNotificationSerializer
from rest_framework.response import Response

class ClientView(APIView):
	def get(self, request):
		client = Client.objects.get(pk=request.user.client.first().id)
		serializer = ClientDetailSerializer(client)
		return Response(serializer.data)

class ClientNotification(APIView):
	def get(self,request):
		loginclient = request.user.client.first()
		notifications = loginclient.notification.all()
		serializer = ClientNotificationSerializer(notifications,many=True)
		return Response(serializer.data)
