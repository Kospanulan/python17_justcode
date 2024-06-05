from django.forms import model_to_dict
from django.http import JsonResponse
from rest_framework import views
from rest_framework.decorators import api_view
from rest_framework.response import Response

from blog.models import Post


@api_view(["GET", "POST"])
def index(request, *args, **kwargs):
    if request.method == "GET":
        posts = Post.objects.all()

        result = [model_to_dict(post) for post in posts]

        return Response(result)

    elif request.method == "POST":
        data = request.data

        new_post = Post(
            title=data["title"],
            content=data["content"],
            author_id=1,
        )

        new_post.save()

        return Response(data)

# for branch 8-drf2
# class PostAPIView(views.APIView):
#
#     def post(self, request, *args, **kwargs):
#         return Response({"detail": "OK!"})


def detail(request, *args, **kwargs):
    post_id = kwargs.get('post_id')
    post = Post.objects.get(id=post_id)

    json_post = model_to_dict(post, fields=["title", "content", "id"])

    return JsonResponse(json_post)

