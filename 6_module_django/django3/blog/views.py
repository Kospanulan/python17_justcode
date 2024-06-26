import django_filters
from rest_framework import generics, permissions

from django_filters import rest_framework as filters

from blog.filters import PostFilterSet
from blog.models import Post
from blog.permissions import IsUser2, IsAdmin, DjangoModelPermissionsWithRead
from blog.serializers import PostSerializer


class PostListCreateAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    permission_classes = [DjangoModelPermissionsWithRead]

    filter_backends = [filters.DjangoFilterBackend]
    # filterset_fields = ['title', 'content']
    # filterset_fields = {
    #     'title': ['exact', 'contains', 'icontains'],
    #     'content': ['exact', 'contains'],
    #     'created_at': ['gte', 'lte']
    # }

    filterset_class = PostFilterSet

    def perform_create(self, serializer):
        print(self.request.user)
        author_id = self.request.user.id
        serializer.save(author_id=author_id)

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     print("query params:", self.request.query_params)
    #
    #     params = self.request.query_params
    #
    #     queryset = queryset.filter(title__icontains=params['title'], content__icontains=params['content'])
    #
    #     return queryset


class PostRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


