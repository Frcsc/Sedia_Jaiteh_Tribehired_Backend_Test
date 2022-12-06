from rest_framework import  viewsets
from rest_framework import permissions
from posts.serializers import PostSerializer
from posts.models import Post
from django.db.models import Count

class PostViewset(viewsets.ReadOnlyModelViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class = PostSerializer
    queryset = Post.objects.annotate(total_number_of_comments=Count('comment')).order_by('-total_number_of_comments')[:10]
