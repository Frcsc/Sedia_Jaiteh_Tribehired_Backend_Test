import requests
from posts.models import Post, Comment

def populate_posts_and_comments():
    posts = requests.get('https://jsonplaceholder.typicode.com/posts').json()
    comments = requests.get('https://jsonplaceholder.typicode.com/comments').json()

    for each_post in posts:
        if not Post.objects.filter_posts(each_post['id'], each_post['userId']).exists():
            Post.objects.create_posts(each_post['id'], each_post['userId'], each_post['title'], each_post['body'])
        Post.objects.filter_posts(each_post['id'], each_post['userId']).update(title=each_post['title'], body=each_post['body'])
    
    for each_comment in comments:
        if not Comment.objects.filter_comments(each_comment['id'], each_comment['postId']).exists():
            Comment.objects.create_comments(
                each_comment['id'],
                each_comment['postId'],
                each_comment['name'],
                each_comment['email'],
                each_comment['body']
                )
        Comment.objects.filter_comments(each_comment['id'], each_comment['postId']).update(name=each_comment['name'], email=each_comment['email'], body=each_comment['body'])  
    return True 