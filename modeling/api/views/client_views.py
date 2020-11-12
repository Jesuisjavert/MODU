from accounts.models import Client
from rest_framework.views import APIView
from ..serializers import ClientDetailSerializer,ClientNotificationSerializer
from rest_framework.response import Response
from ..models import Notification,ProgramRecord,ProgramRecordDetail

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

class ClientNotificationDetail(APIView):
	def put(self,request,pk):
		loginclient = request.user.client.first()
		target_notification = Notification.objects.get(pk=pk)
		if (loginclient == target_notification.client):
			if not(target_notification.is_view):
				target_notification.is_view = True
				target_programrecord = ProgramRecord.objects.get(program=target_notification.program,client=loginclient,is_active=False)
				target_programrecord.now_online_count += 1
				ProgramRecordDetail.objects.create(_type='온라인',content='출석완료',programRecord=target_programrecord)
				if target_programrecord.now_online_count == target_programrecord.max_online_count:
					target_programrecord.is_active = True
					target_programrecord.save()
					target_notification.save()
					return Response({'data':'success','view':'만료되었습니다.'})
				target_notification.save()
				target_programrecord.save()
				return Response({'data': 'success'})
			else:
				return Response({'data':'한번 방문하셨어요.'})
		else:
			return Response({'data':'회원이 다릅니다.'})
