from django.db import models
from django.core import validators

class Post(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField(max_length=550, blank=True)
    is_enabled = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    publish_time = models.DateField(null=True, blank=True)


    def __str__(self):
        return '{}- {}'.format(self.pk, self.title)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField(max_length=250, blank=False)
    is_enabled = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    publish_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.text


