from rest_framework import status
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from ..models import Program
from ..serializers import ProgramSerialiezer
from django.http import Http404

class ProgramView(generics.ListCreateAPIView):
    queryset = Program.objects.all()
    serializer_class = ProgramSerialiezer

    def post(self, request):
        serializer = ProgramSerialiezer(data=request.data)
        if request.user.is_first!=1:
            return Response({"message": "트레이너가 아닙니다"},status=status.HTTP_400_BAD_REQUEST)
        if serializer.is_valid(raise_exception=True):
            serializer.save(trainer_id=request.user.trainer.first().id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProgramDetailView(APIView):

    def get_object(self, pk):
        try:
            return Program.objects.get(pk=pk)
        except Program.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        program = self.get_object(pk)
        serializer = ProgramSerialiezer(program)
        return Response(serializer.data)

    def delete(self, request, pk):
        program = self.get_object(pk)
        if program.trainer.user.id == request.user.id:
            program.delete()
            return Response({"messgae": "삭제 완료"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        program = self.get_object(pk)
        if program.trainer.user.id == request.user.id:
            serializer = ProgramSerialiezer(program, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(trainer_id=request.user.id)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({"message": "수정 실패"}, status=status.HTTP_400_BAD_REQUEST)