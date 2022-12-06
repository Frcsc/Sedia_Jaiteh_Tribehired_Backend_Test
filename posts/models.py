from django.db import models
from tribehired.models import BaseModel
from ckeditor.fields import RichTextField  
from django.contrib.auth import get_user_model
User = get_user_model()


class Post(BaseModel):
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    body = RichTextField()

    def __str__(self):
        return self.title


class Comment(BaseModel):
    postId = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    email = models.EmailField()
    body = RichTextField()


