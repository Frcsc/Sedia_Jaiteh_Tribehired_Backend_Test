from django.urls import include, path, re_path
from posts import api
from rest_framework import routers

app_name = 'posts'

router = routers.DefaultRouter() 
router.register(r'posts', api.PostViewset, basename="posts"),

urlpatterns = [
    path('', include(router.urls)),
]