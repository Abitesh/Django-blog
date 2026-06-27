from django.contrib.auth.models import User
from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer, UserSerializer
from .permissions import IsAuthorOrReadOnly

from rest_framework import viewsets
from rest_framework.decorators import action

class PostViewSet(viewsets.ModelViewSet):
    """
    This ViewSet automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    We'll also add a custom `recent` action below.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        @action(detail=False)
        def recent(self, request):
            """
            Custom endpoint: /api/posts/recent/
            Returns the 5 most recent posts.
            """
            recent_posts = Post.objects.order_by('-created')[:5]
            page = self.paginate_queryset(recent_posts)
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)

            serializer = self.get_serializer(recent_posts, many=True)
            return Response(serializer.data)        

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This ViewSet automatically provides `list` and `retrieve` actions
    for users.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer