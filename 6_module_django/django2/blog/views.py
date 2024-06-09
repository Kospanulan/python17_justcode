from django.forms import model_to_dict
from django.http import JsonResponse
from rest_framework import views, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.views import View, generic


from blog.models import Post
from blog.serializers import PostSerializer


class PostListCreateAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostAPIView(views.APIView):

    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()

        result = PostSerializer(data=posts, many=True)
        result.is_valid()
        return Response(result.data)

    def post(self, request, *args, **kwargs):
        data = request.data

        serializer = PostSerializer(data=data)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)


# class PostRetrieveAPIView(generics.RetrieveAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


class PostRetrieveAPIView(generics.RetrieveAPIView):

    def get(self, request, *args, **kwargs):
        post_id = kwargs.get('pk')
        post = Post.objects.get(id=post_id)

        result = PostSerializer(post, many=False)

        return Response(result.data)

