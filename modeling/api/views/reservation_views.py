from accounts.models import Trainer, Client, User
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from ..serializers import ProgramReservationDaySerializer
from ..models import ProgramReservationDay, ProgramReservationTime, Program
from django.http import Http404

class TrainerReservationView(APIView):
    def post(self, request, pk):
        date = request.POST.get('date')
        start_hour = request.POST.get('time')
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
            print(request.user.id)
            print(User.objects.get(pk=request.user.id).client.all())
            
            ProgramReservationTime.objects.create(
                client = request.user.client.first(),
                ProgramDay = programReservationDay,
                start_hour = start_hour,
                end_hour = "13:00"
            )
            return Response({'data':True,'message':'예약성공'})