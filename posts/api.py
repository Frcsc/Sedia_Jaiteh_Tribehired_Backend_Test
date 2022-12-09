import requests
from rest_framework import  viewsets
from django.db.models import Count
from posts.models import Post, Comment
from posts.filters import CommentFilter
from posts.serializers import PostSerializer, CommentSerializer
from posts.utils import populate_posts_and_comments


class PostViewset(viewsets.ReadOnlyModelViewSet):
    serializer_class = PostSerializer

    def get_queryset(self):
        populate_posts_and_comments()
        return Post.objects.annotate(total_number_of_comments=Count('comment')).order_by('-total_number_of_comments')[:10]


class CommentViewset(viewsets.ReadOnlyModelViewSet):
    serializer_class = CommentSerializer
    filterset_class = CommentFilter

    def get_queryset(self):
        populate_posts_and_comments()
        return Comment.objects.all()
