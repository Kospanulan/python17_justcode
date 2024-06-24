from rest_framework import generics, permissions

from blog.models import Post
from blog.permissions import IsUser2, IsAdmin, DjangoModelPermissionsWithRead
from blog.serializers import PostSerializer


class PostListCreateAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    permission_classes = [DjangoModelPermissionsWithRead]

    def perform_create(self, serializer):
        print(self.request.user)
        author_id = self.request.user.id
        serializer.save(author_id=author_id)


class PostRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


