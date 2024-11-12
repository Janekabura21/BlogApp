from django.db import models
from django.utils.timezone import now

# Create your models here.


class BlogPost(models.Model):
    title = models.CharField(max_length=200)  # Blog post title
    content = models.TextField()  # Main content
    author = models.CharField(max_length=100)  # Author name
    created_at = models.DateTimeField(default=now)  # Creation timestamp
    updated_at = models.DateTimeField(auto_now=True)  # Auto-updated timestamp for edits

    def __str__(self):
        return self.title
