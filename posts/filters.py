from django.db.models import Q
from posts.models import Post, Comment
from django_filters import rest_framework as filters

class CommentFilter(filters.FilterSet):
    
    search = filters.CharFilter(method='filter_search')   
    post = filters.ModelChoiceFilter('postId', to_field_name='id', queryset=Post.objects.all())

    class Meta:
        model = Comment
        fields = ['search']

    def filter_search(self, queryset, name, value):
        return queryset.filter(
            Q(id__iexact=value) |
            Q(name__icontains=value) |
            Q(email__icontains=value) |
            Q(body__icontains=value) 
        )
