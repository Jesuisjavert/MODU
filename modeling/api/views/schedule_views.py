from rest_framework.views import APIView
from rest_framework.response import Response
from ..models import ProgramReservationDay,ProgramReservationTime
from ..serializers import ProgramReservationTimeSerializer

class ScheduleList(APIView):
    def get(self,request):
        if request.user.trainer.exists():
            logintrainer = request.user.trainer.first()
            trainerprograms = logintrainer.program.all()
            programrest = []
            for trainerprogram in trainerprograms:
                templist = trainerprogram.programreservationday.values_list('id',flat=True)
                programrest.extend(templist)
            result = []
            for prog in programrest:
                proge = ProgramReservationDay.objects.get(id=prog)
                temp = proge.programreservationtime.values_list('id',flat=True)
                result.extend(temp)
            a = ProgramReservationTime.objects.filter(id__in=result)
            serializer = ProgramReservationTimeSerializer(a,many=True)
            return Response(serializer.data)

                

