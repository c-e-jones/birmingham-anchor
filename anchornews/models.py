from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    # This is the data model for posts
    title = models.CharField(
        max_length=150
    )
    slug = models.SlugField(
        max_length=200, unique_for_date='created-on'
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True
    )
    genre = models.CharField(
        max_length=50, choices=[
            ("Local Government", "Local Government"),
            ("National News", "National News"),
            ("Tech", "Tech"),
            ("Local Events", "Local Events"),
            ("Reguional Affairs", "Regional Affairs"),
            ("Business", "Business"),
            ("Food", "Food"),
            ("Tourism", "Tourism"),
            ("Sports", "Sports"),
            ("Arts and Culture", "Arts and Culture"),
            ("Finance", "Finance"),
            ("Crime", "Crime")
        ])
    byline = models.CharField(max_length=150)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    objects = models.Manager()
    published = Published()

class Published(models.Manager):
    # This allows the retrieval of published posts
    def get_queryset(self) -> models.QuerySet:
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)
    