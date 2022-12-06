from django.contrib import admin
from posts.models import Post, Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ['userId', 'title', 'created_at']
    search_fields = ['title']
admin.site.register(Post, PostAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ['email', 'name', 'created_at']
    search_fields = ['email', 'name',]
admin.site.register(Comment, CommentAdmin)

