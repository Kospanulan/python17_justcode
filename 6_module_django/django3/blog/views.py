from rest_framework import generics, permissions, authentication

from blog.models import Post
from blog.serializers import PostSerializer


class PostListCreateAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        # serializer.validated_data['author_id'] = 1
        print(self.request.user)
        author_id = self.request.user.id
        serializer.save(author_id=author_id)

    def get_queryset(self):
        queryset = Post.objects.all().filter(author_id=self.request.user.id)
        return queryset


class PostRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer