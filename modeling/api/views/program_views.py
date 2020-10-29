from rest_framework import status
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from ..models import Program
from ..serializers import ProgramSerialiezer

class ProgramView(generics.ListCreateAPIView):
    queryset = Program.objects.all()
    serializer_class = ProgramSerialiezer

    def post(self, request):
        serializer = ProgramSerialiezer(data=request.data)
        if request.user.is_first!=1:
            return Response({"message": "트레이너가 아닙니다"},status=status.HTTP_400_BAD_REQUEST)

        if serializer.is_valid(raise_exception=True):
            serializer.save(trainer_id=request.user.id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProgramDetailView(APIView):
    def get(self, request, pk):
        program = Program.objects.get(pk=pk)
        serializer = ProgramSerialiezer(program)
        return Response(serializer.data)