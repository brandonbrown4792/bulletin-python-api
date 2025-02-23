from django.db import models

class Post(models.Model):
    author = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField(null=True, blank=True)
    image = models.TextField(null=True, blank=True)
    is_news_story = models.BooleanField(default=False)
    source = models.CharField(max_length=200, null=True, blank=True)
    title = models.CharField(max_length=200)
    updated_at = models.DateTimeField(auto_now=True)
    url = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title
