from django.contrib import admin
from .models import Catalog, Tag

admin.site.register(Tag)

@admin.register(Catalog)
class CatalogAdmin(admin.ModelAdmin):
    list_display = ('title', 'published', 'author')
    date_hierarchy = 'published'
    search_fields = ('title', 'description')