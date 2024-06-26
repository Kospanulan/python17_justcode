from django_filters import rest_framework as filters

from blog.models import Post


class PostFilterSet(filters.FilterSet):

    start_date = filters.DateTimeFilter(field_name='created_at', lookup_expr='gte')
    end_date = filters.DateTimeFilter(field_name='created_at', lookup_expr='lte')

    class Meta:
        model = Post
        fields = {
            'title': ['exact', 'contains', 'icontains'],
            'content': ['exact', 'contains']
        }

