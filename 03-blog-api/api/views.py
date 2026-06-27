from rest_framework import status
from rest_framework.response import Response

from .models import Post
from .serializers import PostSerializer

from django.http import Http404
from rest_framework.views import APIView

from rest_framework import generics

from django.contrib.auth.models import User
from .serializers import PostSerializer, UserSerializer

from rest_framework import permissions
from .permissions import IsAuthorOrReadOnly

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer