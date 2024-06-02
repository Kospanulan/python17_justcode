from django import views
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.template import loader
from django.views import generic
from django.views.generic import ListView

from blog.forms import PostModelForm
from blog.models import Post, Comment


# class OurListView(views.View):
#     model = None
#     context_object_name = None
#     template_name = None
#
#     def get_queryset(self):
#         return self.model.objects.all()
#
#     def get_context_data(self):
#         objects = self.get_queryset()
#
#         return {
#             self.context_object_name: objects,
#         }
#
#     def get(self, request, *args, **kwargs):
#
#         context = self.get_context_data()
#
#         return render(
#             request=request,
#             template_name=self.template_name,
#             context=context
#         )


class PostListView(generic.ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'my_posts'

    # def get_queryset(self):
    #     return Post.objects.filter(pk=1)
    #
    # def get_context_data(self):
    #     context = super().get_context_data()
    #     context["user"] = "Ulan"
    #     return context


# class CommentListView(OurListView):
#     model = Comment
#     template_name = 'blog/index.html'
#     context_object_name = 'my_posts'





















    # def get_queryset(self):
    #     return Post.objects.filter(pk=4)
    #
    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data()
    #     context['user'] = "Ashat"
    #     return context










class PostCreateView(views.View):

    def get(self, request, *args, **kwargs):
        context = {
            'my_form': PostModelForm()
        }
        return render(
            request=request,
            template_name='blog/create_post.html',
            context=context
        )

    def post(self, request, *args, **kwargs):
        form = PostModelForm(request.POST)

        if form.is_valid():
            new_post = form.save()

            return redirect("post-detail", new_post.pk)


def detail(request, *args, **kwargs):
    post_id = kwargs.get("post_id")
    post = Post.objects.get(pk=post_id)
    return HttpResponse(f"<h1>{post.pk}.{post.title}</h1>"
                        f"<p>{post.content}</p>")


def comment(request, *args, **kwargs):
    comments = Comment.objects.get(pk=1)
    return HttpResponse(f"<p>{comments.text}</p>")

