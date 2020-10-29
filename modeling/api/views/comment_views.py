from accounts.models import Trainer, Client
from rest_framework import status
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from ..serializers import TrainerSerializer, TrainerCommentSerializer
from ..models import TrainerComment

class TrainerView(generics.ListAPIView):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer

class TrainerDetailView(APIView):
    def get(self, request, pk):
        trainer = Trainer.objects.get(pk=pk)
        serializer = TrainerSerializer(trainer)
        return Response(serializer.data)

    def put(self, request, pk):
        trainer = Trainer.objects.get(pk=pk)
        serializer = TrainerSerializer(trainer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TrainerCommentView(generics.ListCreateAPIView):
    queryset = TrainerComment.objects.all()
    serializer_class = TrainerCommentSerializer

    def post(self, request, pk, format=None):
        serializer = TrainerCommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(trainer_id=pk, client_id=request.user.id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TrainerCommentDetailView(APIView):
    def get(self, request, pk):
        comment = TrainerComment.objects.get(pk=pk)
        serializer = TrainerCommentSerializer(comment)
        return Response(serializer.data)

    def delete(self, request, pk):
        comment = TrainerComment.objects.get(pk=pk)
        if comment.user == request.user:
            comment.delete()
            return Response({"message": "삭제 성공"}, status=status.HTTP_201_CREATED)
        return Response({"message": "삭제 실패"}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        comment = TrainerComment.objects.get(pk=pk)
        if comment.client.user == request.user:
            serializer = TrainerCommentSerializer(comment, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(trainer_id=comment.trainer.id, client_id=request.user.id)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({"message": "수정 실패"}, status=status.HTTP_400_BAD_REQUEST)
