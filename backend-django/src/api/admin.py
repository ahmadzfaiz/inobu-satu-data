from django.contrib import admin
from .models import Article

@admin.register(Article)
class ArticleModel(admin.ModelAdmin):
    list_filter = ('title'  'author')
    list_display = ('title'  'author'  'description')