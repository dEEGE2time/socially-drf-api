from django.db.models import Count
from rest_framework import generics, permissions, filters
from .models import Post
from .serializers import PostSerializer
from drf_api.permissions import IsOwnerOrReadOnly


class PostList(generics.ListCreateAPIView):
    """
    View all posts in database
    Create post if user is authenticated.
    """
    serializer_class = PostSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    queryset = Post.objects.annotate(
        likes_count=Count('likes', distinct=True),
        comments_count=Count('comment', distinct=True),
    ).order_by('-created_on')
    filter_backends = [
        filters.OrderingFilter
    ]
    ordering_fields = [
        'likes_count',
        'comments_count',
        'likes__created_on',
        'comment__created_on',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    View each post individually
    Update, edit or delete post if user = owner
    """
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Post.objects.annotate(
        likes_count=Count('likes', distinct=True),
        comments_count=Count('comment', distinct=True),
    ).order_by('-created_on')