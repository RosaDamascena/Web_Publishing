from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=250)

class Post(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE
    )
    content = models.TextField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)


