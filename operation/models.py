from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=20, blank=False)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        return super(Tag, self).save(*args, **kwargs)

class Catalog(models.Model):
    LIST_CATEGORY_CHOICES = [
        ('JSON', 'JavaScript Object Notation (JSON)'),
        ('XML', 'Extensible Markup Language (XML)'),
        ('WFS', 'Web Feature Service (WFS)'),
        ('WMS', 'Web Map Service (WMS)'),
        ('WMTS', 'Web Map Tile Service (WMTS)'),
        ('XYZ', 'XYZ Tile Layer')
    ]

    title = models.CharField(max_length=200, blank=False)
    category = models.CharField(max_length=50, choices=LIST_CATEGORY_CHOICES, default='JSON')
    tags = models.ManyToManyField(Tag)
    url = models.URLField(max_length=200, unique=True, blank=False)
    description = models.TextField(blank=False)
    slug = models.SlugField(max_length=100, unique=True)
    published = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Dashboard(models.Model):
    title = models.CharField(max_length=200, blank=False)
    tags = models.ManyToManyField(Tag)
    url = models.URLField(max_length=200, unique=True, blank=False)
    description = models.TextField(blank=False)
    slug = models.SlugField(max_length=100, unique=True)
    published = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Document(models.Model):
    LIST_CATEGORY_CHOICES = [
        ('document', 'Document format (.doc)'),
        ('spreadsheet', 'Spreadsheet format (.xls)'),
        ('presentation', 'Presentation format (.ppt)'),
        ('portable', 'Portable document format (.pdf)'),
    ]

    title = models.CharField(max_length=200, blank=False)
    category = models.CharField(max_length=50, choices=LIST_CATEGORY_CHOICES, default='document')
    tags = models.ManyToManyField(Tag)
    url = models.URLField(max_length=200, unique=True, blank=False)
    description = models.TextField(blank=False)
    slug = models.SlugField(max_length=100, unique=True)
    published = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title