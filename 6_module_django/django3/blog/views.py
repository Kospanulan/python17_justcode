from rest_framework import generics, permissions, authentication
from rest_framework_simplejwt.authentication import JWTAuthentication

from blog.models import Post
from blog.serializers import PostSerializer


class PostListCreateAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        print(self.request.user)
        author_id = self.request.user.id
        serializer.save(author_id=author_id)

    def get_queryset(self):
        queryset = Post.objects.all().filter(author_id=self.request.user.id)
        return queryset


class PostRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer