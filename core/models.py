from django.db import models
from django.contrib.auth.models import User
from django_extensions.db.fields import AutoSlugField


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    slug = AutoSlugField(populate_from='title',
                         unique=True, null=True, blank=True)
    postImage = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.title
