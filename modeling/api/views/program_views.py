from rest_framework import status
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from ..models import Program,ProgramPrice,ProgramSchedule,ProgramWebRtc,Notification
from ..serializers import ProgramSerialiezer, ClientSerializer, ProgramUserSerialiezr,ProgramOnlieSerialiezer
from django.http import Http404
from accounts.models import Tag
from datetime import datetime
class ProgramView(generics.ListCreateAPIView):
    # 프로그램 GET 정보가져오기
    queryset = Program.objects.all()
    serializer_class = ProgramSerialiezer

    # 프로그램 생성
    def post(self, request):
        serializer = ProgramSerialiezer(data=request.data)
        if request.user.is_first!=1:
            return Response({"message": "트레이너가 아닙니다"},status=status.HTTP_400_BAD_REQUEST)
        if serializer.is_valid(raise_exception=True):
            saved_program = serializer.save(trainer_id=request.user.trainer.first().id)
            k = dict(request.data)
            programdetail = []
            tags = request.data['tags'].split(',')
            for eachtag in tags:
                saved_program.tags.add(Tag.objects.get(name=eachtag))
            for keydata in k.keys():
                if 'program_detail' in keydata:
                    key_index = int(keydata.replace('program_detail[','').split(']')[0])
                    key_data = keydata.replace('program_detail[','').split(']')[1].replace('[','')
                    if len(programdetail) < key_index+1:
                        programdetail.append({
                            key_data : k[keydata][0]
                        })
                    else:
                        programdetail[key_index][key_data] = k[keydata][0]
            for eachdata in programdetail:
                ProgramPrice.objects.create(title=eachdata['title'],online_count=int(eachdata['online_count']),price=int(eachdata['price']),program=saved_program,offline_count=int(eachdata['offline_count']))
                    
                    
        
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProgramDetailView(APIView):
    def get_object(self, pk):
        try:
            return Program.objects.get(pk=pk)
        except Program.DoesNotExist:
            raise Http404

    # 프로그램 디테일
    def get(self, request, pk):
        program = self.get_object(pk)
        serializer = ProgramSerialiezer(program)
        return Response(serializer.data)

    # 프로그램 삭제
    def delete(self, request, pk):
        program = self.get_object(pk)
        if program.trainer.user.id == request.user.id:
            program.delete()
            return Response({"messgae": "삭제 완료"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # 프로그램 수정
    def put(self, request, pk):
        program = self.get_object(pk)
        if program.trainer.user.id == request.user.id:
            serializer = ProgramSerialiezer(program, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(trainer_id=request.user.id)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({"message": "수정 실패"}, status=status.HTTP_400_BAD_REQUEST)

class OnlineProgramSchedule(APIView):
    def post(self,request,pk):
        onlineprogram = Program.objects.get(id=pk)
        for schedule in request.data['schedule']:
            if schedule['disabled'] == False:
                ProgramSchedule.objects.create(day=schedule['day'],start_hour=schedule['start_hour'],end_hour=schedule['end_hour'],program=onlineprogram)
                return Response({'data': True})

class TrainerProgramView(APIView):
    def get(self, request):
        try:
            trainer = request.user.trainer.first()
            programs = trainer.program.all()
            serializer = ProgramSerialiezer(programs, many=True)
            return Response(serializer.data)
        except:
            return Response({"message": "트레이너가 아닙니다"},status=status.HTTP_400_BAD_REQUEST)

class ProgramUserView(APIView):
    def get(self, request, pk):
        program = Program.objects.get(pk=pk)
        clients = program.programpayment.all()
        serializer = ProgramUserSerialiezr(clients, many=True)
        return Response(serializer.data)



class TrainerOnlineProgramView(APIView):
    def get(self, request):
        try:
            trainer = request.user.trainer.first()
            programs = trainer.program.all()
            serializer = ProgramOnlieSerialiezer(programs, many=True)
            return Response(serializer.data)
        except:
            return Response({"message": "트레이너가 아닙니다"},status=status.HTTP_400_BAD_REQUEST)
    def post(self,request):
        today = datetime.today().strftime("%Y-%m-%d")
        webRtcfind = ProgramWebRtc.objects.filter(program_id=request.data['program_id']).filter(create_at=today)
        if webRtcfind.exists():
            return Response({'data':webRtcfind.first().webrtcroomId ,'is_first': False})
        else:
            webRtc = ProgramWebRtc.objects.create(program_id=request.data['program_id'],webrtcroomId = request.data['webRtcroomId'] )
            programrecords = webRtc.program.programrecord.all()
            for programrecord in programrecords:
                listenclient = programrecord.client
                Notification.objects.create(webrtcroomId=webRtc.webrtcroomId,client=listenclient,program=webRtc.program)
            return Response({'data' : webRtc.webrtcroomId,'is_first' : True})
        return Response({'data':True})