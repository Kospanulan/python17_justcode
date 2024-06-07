from django.forms import model_to_dict
from django.http import JsonResponse
from rest_framework import views
from rest_framework.decorators import api_view
from rest_framework.response import Response

from blog.models import Post
from blog.serializers import PostSerializer


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


def detail(request, *args, **kwargs):
    post_id = kwargs.get('post_id')
    post = Post.objects.get(id=post_id)

    json_post = model_to_dict(post, fields=["title", "content", "id"])

    return JsonResponse(json_post)

