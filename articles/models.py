from django.db import models
from django.urls import reverse
from users.models import CustomUser


class Tag(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.name
    

class Article(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True)
    tags = models.ManyToManyField(Tag, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('articles:detail', kwargs={'pk': self.pk})


