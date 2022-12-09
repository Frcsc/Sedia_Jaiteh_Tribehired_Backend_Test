from django.db import models
from tribehired.models import BaseModel
from ckeditor.fields import RichTextField 

class PostManager(models.Manager):

    def filter_posts(self, id, userId):
        return (
            super()
            .get_queryset()
            .filter(
                id=id,
                userId=userId
            )
        )

    def create_posts(self, id, userId, title, body):
        data = {
            'id': id,
            'userId': userId,
            'title': title,
            'body': body
        }
        return self.create(**data)

class Post(BaseModel):
    id = models.IntegerField(primary_key=True)
    userId = models.IntegerField()
    title = models.CharField(max_length=128)
    body = RichTextField()

    def __str__(self):
        return self.title

    objects: PostManager
    objects = PostManager()

class CommentManager(models.Manager):
    def filter_comments(self, id, post_id):
        return (
            super()
            .get_queryset()
            .filter(
                id=id,
                postId=Post.objects.get(id=post_id)
            )
        )

    def create_comments(self, id, postId, name, email, body):
        data = {
            'postId': Post.objects.get(id=postId),
            'id': id,
            'name': name,
            'email': email,
            'body': body
        }
        return self.create(**data)

class Comment(BaseModel):
    postId = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    email = models.EmailField()
    body = RichTextField()


    objects: CommentManager
    objects = CommentManager()