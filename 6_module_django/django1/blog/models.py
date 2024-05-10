from django.db import models


class Post(models.Model):

    title = models.CharField(max_length=100)  # VARCHAR(100) NOT NULL
    content = models.TextField()  # TEXT NOT NULL

    def __str__(self):
        return f"{self.title} ({self.pk})"  # pk = primary key


class Comment(models.Model):

    post = models.ForeignKey(Post, on_delete=models.CASCADE)  # related_name: comment_set
    text = models.CharField(max_length=200)  # VARCHAR NOT NULL

    def __str__(self):
        return f"{self.text} ({self.pk})"
