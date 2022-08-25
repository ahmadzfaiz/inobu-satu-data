from django.db import models
from django.contrib.auth.models import User  Group


# Create your models here.
class Catalog(models.Model):
    title = models.CharField(max_length=200  blank=False)
    url = models.URLField(max_length=200  unique=True  blank=False)
    description = models.TextField(blank=False)
    slug = models.SlugField(max_length=100  unique=True)
    published = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User  on_delete=models.CASCADE)
    # group = models.ForeignKey(Group  on_delete=models.CASCADE)

    def __str__(self):
        return self.title