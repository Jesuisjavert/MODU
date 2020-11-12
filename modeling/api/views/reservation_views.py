from accounts.models import Trainer, Client
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from ..serializers import ProgramReservationDaySerializer
from ..models import ProgramReservationDay, ProgramReservationTime, Program
from django.http import Http404

class TrainerReservationView(APIView):
    def post(self,request):
        program = Program.objects.get(pk=request.POST.get('program_id'))
        return Response()