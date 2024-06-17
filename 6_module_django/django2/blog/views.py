from django.forms import model_to_dict
from django.http import JsonResponse
from rest_framework import views, generics, mixins, permissions, authentication
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.views import View, generic


from blog.models import Post
from blog.serializers import PostSerializer


class PostListCreateAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # serializer.validated_data['author_id'] = 1
        print(self.request.user)
        author_id = self.request.user.id
        serializer.save(author_id=author_id)


class PostRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


# class PostCRUDView(
#     mixins.ListModelMixin,
#     mixins.CreateModelMixin,
#     mixins.RetrieveModelMixin,
#     mixins.UpdateModelMixin,
#     mixins.DestroyModelMixin,
#     generics.GenericAPIView
# ):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#
#     def get(self, request, *args, **kwargs):
#         if kwargs.get('pk'):
#             return self.retrieve(request, *args, **kwargs)
#
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def patch(self, request, *args, **kwargs):
#         return self.partial_update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)
