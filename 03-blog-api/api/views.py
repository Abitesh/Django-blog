from rest_framework import status
from rest_framework.response import Response

from .models import Post
from .serializers import PostSerializer

from django.http import Http404
from rest_framework.views import APIView

from rest_framework import generics

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer