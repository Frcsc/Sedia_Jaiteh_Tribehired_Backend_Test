from django.db.models import Q
from posts.models import Post, Comment
from django_filters import rest_framework as filters

class CommentFilter(filters.FilterSet):
    '''
        comments can also be filtered using a related Post object. The line below show an implementation of this.
        post = filters.ModelChoiceFilter('postId', to_field_name='id', queryset=Post.objects.all())
    '''

    search = filters.CharFilter(method='filter_search')

    class Meta:
        model = Comment
        fields = ['search']

    def filter_search(self, queryset, name, value):
        return queryset.filter(
            Q(postId__id__icontains=value) |
            Q(id__icontains=value) |
            Q(name__icontains=value) |
            Q(email__icontains=value) |
            Q(body__icontains=value) 
        )
