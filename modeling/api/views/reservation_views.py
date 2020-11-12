from accounts.models import Trainer, Client, User
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from ..serializers import ProgramReservationDaySerializer
from ..models import ProgramReservationDay, ProgramReservationTime, Program, ProgramRecord
from django.http import Http404

class TrainerReservationView(APIView):
    def post(self, request, pk):
        date = request.POST.get('date')
        start_hour = request.POST.get('time')
        client = request.user.client.first()
        print(date)
        program = Program.objects.get(pk=request.POST.get('program_id'))
        if not program.programreservationday.filter(day=date).exists():
            ProgramReservationDay.objects.create(
                program = program,
                day = date
            )

        programReservationDay = program.programreservationday.filter(day=date).first()

        if programReservationDay.programreservationtime.filter(start_hour=start_hour).exists():
            return Response({'data':False,'message':'예약불가'})
        else:
            ProgramReservationTime.objects.create(
                client = client,
                ProgramDay = programReservationDay,
                start_hour = start_hour,
                end_hour = "13:00"
            )
            target_programrecord = ProgramRecord.objects.get(program=program, client=client, is_active=False)
            target_programrecord.now_offline_count += 1
            ProgramRecordDetail.objects.create(_type='오프라인',content='출석완료',programRecord=target_programrecord)
            if target_programrecord.now_offline_count == target_programrecord.max_offline_count:
                target_programrecord.is_active = True
                target_programrecord.save()
            return Response({'data':True,'message':'예약성공'})