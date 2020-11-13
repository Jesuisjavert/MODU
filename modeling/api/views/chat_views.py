from rest_framework.views import APIView
from rest_framework.response import Response
import base64
from ..models import ChatRoom,Program
from Crypto import Random
from Crypto.Cipher import AES


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
        