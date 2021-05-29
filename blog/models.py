from django.db import models
from profiles.models import UserProfile


# https://djangocentral.com/building-a-blog-application-with-django/


class Post(models.Model):
    image = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=200, unique=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
