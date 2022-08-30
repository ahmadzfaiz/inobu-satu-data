from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=20, blank=False)

    def __str__(self):
        return self.name

class Catalog(models.Model):
    title = models.CharField(max_length=200, blank=False)
    tags = models.ManyToManyField(Tag)
    url = models.URLField(max_length=200, unique=True, blank=False)
    description = models.TextField(blank=False)
    slug = models.SlugField(max_length=100, unique=True)
    published = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title