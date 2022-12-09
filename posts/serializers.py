from rest_framework import serializers
from posts.models import Post, Comment

class PostSerializer(serializers.ModelSerializer):

    total_number_of_comments = serializers.IntegerField(read_only=True)

    class Meta:
        model = Post
        fields = ['userId', 'id', 'title', 'body', 'total_number_of_comments']


class CommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        fields = ['postId', 'id', 'name', 'email', 'body']