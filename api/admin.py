from django.contrib import admin
from .models import Article, Petani

@admin.register(Article)
class ArticleModel(admin.ModelAdmin):
    list_filter = ('title', 'author')
    list_display = ('title', 'author', 'description')

@admin.register(Petani)
class PetaniModel(admin.ModelAdmin):
    search_fields = ('nik', 'nama_lengkap')
    list_filter = ('gelar_depan', 'gelar_belakang', 'jenis_kelamin', 'desa', 'kecamatan', 'kabupaten')
    list_display = ('nik', 'nama_lengkap', 'jenis_kelamin', 'id')
    ordering = ('nik', 'nama_lengkap')