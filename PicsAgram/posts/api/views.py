from .permissions import IsAuthorOrReadOnly
from posts.models import Answer, Post
from rest_framework import generics
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .serializers import AnswerSerializer, PostDescriptionSerializer, PostSerializer
from django.shortcuts import get_object_or_404


class PostAPIView(ModelViewSet):
    
    queryset = Post.objects.all().order_by("-created_at")
    serializer_class = PostSerializer
    permission_classes = [IsAuthorOrReadOnly, IsAuthenticated]

    def perform_create(self, serializer):
        author = self.request.user
        serializer.save(author=author)


class PostLikeAPIView(APIView):

    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        user = self.request.user

        post.voters.add(user)
        
        context = { "request":  request }
        serializer = self.serializer_class(post, context=context)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        user = self.request.user

        post.voters.remove(user)
        
        context = { "request":  request }
        serializer = self.serializer_class(post, context=context)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AnswerCreateAPIView(generics.CreateAPIView):
    
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        pk = self.kwargs.get("pk")
        post = get_object_or_404(Post, pk=pk)
        user = self.request.user

        serializer.save(post=post, author=user)


class AnswersListAPIView(generics.ListAPIView):

    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        return Answer.objects.filter(post__pk=pk).order_by("-created_at")


class AnswerRUDAPIView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]


class UpdatePostDescriptionAPIView(generics.UpdateAPIView):

    queryset = Post.objects.all()
    serializer_class = PostDescriptionSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
