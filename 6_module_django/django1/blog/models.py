from django.db import models

"""
Posts
Categories

post_categories: id, post_id, category_id


"""


class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.pk})"


class Post(models.Model):

    title = models.CharField(max_length=100)  # VARCHAR(100) NOT NULL
    content = models.TextField()  # TEXT NOT NULL UNIQUE

    categories_custom = models.ManyToManyField(Category, through="PostCategoriesCustom", related_name="posts")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def demo_text(self):
        return f"{self.content[:10]}..."

    def __str__(self):
        return f"{self.title} ({self.pk})"  # pk = primary key


class PostCategoriesCustom(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")  # related_name: comment_set
    text = models.CharField(max_length=200)  # VARCHAR NOT NULL

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.text} ({self.pk})"
