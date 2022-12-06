from rest_framework import serializers
from posts.models import Post

class PostSerializer(serializers.ModelSerializer):

    total_number_of_comments = serializers.IntegerField()

    class Meta:
        model = Post
        fields = ['id','title', 'body', 'total_number_of_comments']