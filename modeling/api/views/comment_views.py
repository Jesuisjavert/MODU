from accounts.models import Trainer, Client
from rest_framework import status
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from ..serializers import TrainerSerializer, TrainerCommentSerializer, ProgramCommentSerializer
from ..models import TrainerComment, ProgramComment, Program
from django.http import Http404

class TrainerView(generics.ListAPIView):
    # 트레이너 전체정보
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer

class TrainerDetailView(APIView):
    # 트레이너 디테일
    def get(self, request, pk):
        trainer = Trainer.objects.get(pk=pk)
        serializer = TrainerSerializer(trainer)
        return Response(serializer.data)

    # 트레이너 정보 수정
    def put(self, request, pk):
        trainer = Trainer.objects.get(pk=pk)
        serializer = TrainerSerializer(trainer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TrainerCommentView(APIView):
    # 트레이너 댓글 가져오기
    def get(self, reuqest, pk):
        comment = Trainer.objects.get(pk=pk).trainercomment.all()
        serializer = TrainerCommentSerializer(comment, many=True)
        return Response(serializer.data)

    # 트레이너 댓글 작성
    def post(self, request, pk, format=None):
        serializer = TrainerCommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(trainer_id=pk, client_id=request.user.client.first().id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TrainerCommentDetailView(APIView):
    # 트레이너 댓글 디테일
    def get(self, request, pk):
        comment = TrainerComment.objects.get(pk=pk)
        serializer = TrainerCommentSerializer(comment)
        return Response(serializer.data)

    # 트레이너 댓글 삭제
    def delete(self, request, pk):
        comment = TrainerComment.objects.get(pk=pk)
        if comment.client.user.id == request.user.id:
            comment.delete()
            return Response({"message": "삭제 성공"}, status=status.HTTP_201_CREATED)
        return Response({"message": "삭제 실패"}, status=status.HTTP_400_BAD_REQUEST)

    # 트레이너 댓글 수정
    def put(self, request, pk):
        comment = TrainerComment.objects.get(pk=pk)
        if comment.client.user == request.user:
            serializer = TrainerCommentSerializer(comment, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(trainer_id=comment.trainer.id, client_id=request.user.id)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({"message": "수정 실패"}, status=status.HTTP_400_BAD_REQUEST)

class ProgramCommentView(APIView):
    def get_object(self, pk):
        try:
            return Program.objects.get(pk=pk)
        except Program.DoesNotExist:
            raise Http404
        
    # 프로그램 댓글
    def get(self, request, pk):
        comment = self.get_object(pk).programcomment.all()
        serializer = ProgramCommentSerializer(comment, many=True)
        return Response(serializer.data)

    # 프로그램 댓글 작성
    def post(self, request, pk):
        program = Program.objects.get(pk=pk)
        serializer = ProgramCommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(program_id=pk, client_id=request.user.client.first().id, trainer_id=program.trainer.id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProgramCommentDetailView(APIView):
    def get_object(self, pk):
        try:
            return ProgramComment.objects.get(pk=pk)
        except ProgramComment.DoesNotExist:
            raise Http404
    
    # 프로그램 댓글 디테일
    def get(self, request, pk):
        programcomment = self.get_object(pk)
        serializer = ProgramCommentSerializer(programcomment)
        return Response(serializer.data)

    # 프로그램 댓글 삭제
    def delete(self, request, pk):
        programcomment = self.get_object(pk)
        if programcomment.client.user.id == request.user.id:
            programcomment.delete()
            return Response({"message": "삭제 성공"}, status=status.HTTP_201_CREATED)
        return Response({"message": "삭제 실패"}, status=status.HTTP_400_BAD_REQUEST)

    # 프로그램 댓글 수정
    def put(self, request, pk):
        programcomment = self.get_object(pk)
        if programcomment.client.user.id == request.user.id:
            serializer = ProgramCommentSerializer(programcomment, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(program_id=pk, client_id=request.user.client.first().id, trainer_id=programcomment.trainer.id)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({"message": "수정 실패"}, status=status.HTTP_400_BAD_REQUEST)
