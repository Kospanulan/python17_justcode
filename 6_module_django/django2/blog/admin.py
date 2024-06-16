from django.contrib import admin

from blog.models import Post, User

# Register your models here.

admin.site.register(Post)
admin.site.register(User)
