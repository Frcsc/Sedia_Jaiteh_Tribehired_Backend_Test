from rest_framework import  viewsets
from django.db.models import Count
from posts.models import Post, Comment
from posts.filters import CommentFilter
from posts.serializers import PostSerializer, CommentSerializer


class PostViewset(viewsets.ReadOnlyModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.annotate(total_number_of_comments=Count('comment')).order_by('-total_number_of_comments')[:10]


class CommentViewset(viewsets.ReadOnlyModelViewSet):
    serializer_class = CommentSerializer
    filterset_class = CommentFilter
    queryset = Comment.objects.all()
