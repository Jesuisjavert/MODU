from rest_framework.views import APIView
from rest_framework.response import Response
import base64
from ..models import ChatRoom,Program,ChatLog
from Crypto import Random
from Crypto.Cipher import AES
from ..serializers import ChatLogSerializer,ChatRoomSerializer


BS = 16
pad = lambda s: s + (BS - len(s.encode('utf-8')) % BS) * chr(BS - len(s.encode('utf-8')) % BS)
unpad = lambda s : s[:-ord(s[len(s)-1:])]


class AESCipher:
    def __init__( self, key ):
        self.key = key

    def encrypt( self, raw ):
        raw = pad(raw)
        iv = b'\x11\xefC_t\xb7\xc090\xa9P&5/\xf7\x8d'
        cipher = AES.new( self.key, AES.MODE_CBC, iv )
        return base64.b64encode( iv + cipher.encrypt( raw.encode('utf-8') ) )

    def decrypt( self, enc ):
        enc = base64.b64decode(enc)
        iv = enc[:16]
        cipher = AES.new(self.key, AES.MODE_CBC, iv )
        return unpad(cipher.decrypt( enc[16:] ))


key = [0x10, 0x01, 0x15, 0x1B, 0xA1, 0x11, 0x57, 0x72, 0x6C, 0x21, 0x56, 0x57, 0x62, 0x16, 0x05, 0x3D,
        0xFF, 0xFE, 0x11, 0x1B, 0x21, 0x31, 0x57, 0x72, 0x6B, 0x21, 0xA6, 0xA7, 0x6E, 0xE6, 0xE5, 0x3F]



class ChatRooms(APIView):
    def get(self,request):
        targetuser = request.user
        chatrooms = ChatRoom.objects.filter(trainer=targetuser.trainer.first())
        serializer = ChatRoomSerializer(chatrooms,many=True)

        return Response(serializer.data)
    def post(self,reqeust):
        program_id = reqeust.data['program_id']
        trainer = Program.objects.get(id=program_id).trainer
        client = reqeust.user.username
        total = str(trainer.id)+client
        roomId = AESCipher(bytes(key)).encrypt(total)
        if ChatRoom.objects.filter(roomid=roomId).exists():
            return Response({'roomId':roomId})
        else:
            ChatRoom.objects.create(
                roomid = roomId,
                client = reqeust.user.client.first(),
                trainer = trainer )
            return Response({'roomId':roomId})


class ChatLogs(APIView):
    def get(self,request):
        if request.user.is_authenticated:
            roomId = request.GET.get('roomId')
            user = request.user
            if user.trainer.all().exists():
                _type = '트레이너'
            elif user.client.all().exists():
                _type = '클라이언트'
            else:
                return Response({'data':'잘못 들어오셨네요.'})
            try:
                if _type == '트레이너':
                    targetchatroom = ChatRoom.objects.get(roomid__contains=roomId,trainer=user.trainer.first())
                elif _type == '클라이언트':
                    targetchatroom = ChatRoom.objects.get(roomid__contains=roomId,client=user.client.first())
                chattinglog = ChatLog.objects.filter(chatroom=targetchatroom)
                serializer = ChatLogSerializer(chattinglog,many=True)
                return Response(serializer.data)
            except:
                return Response({'data':'채팅창에 접근권한이 없습니다.'})
        else:
            return Response({'data':'Login을 하세요.'})
    def post(self,request):
        roomId = request.data['chatroomId']
        username = request.data['username']
        message = request.data['message']
        time =  request.data['time']
        targetchatroom = ChatRoom.objects.get(roomid__contains=roomId)
        data = ChatLog.objects.create(username=username,
        message=message,
        time=time,
        chatroom=targetchatroom)
        return Response({'data':True})