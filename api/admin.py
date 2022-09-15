from django.contrib import admin
from .models import *

@admin.register(Article)
class ArticleModel(admin.ModelAdmin):
    list_filter = ('title', 'author')
    list_display = ('title', 'author', 'description')

@admin.register(Petani)
class PetaniModel(admin.ModelAdmin):
    search_fields = ('nik', 'nama_lengkap')
    list_filter = ('gelar_depan', 'gelar_belakang', 'jenis_kelamin', 'desa', 'kecamatan', 'kabupaten')
    list_display = ('nik', 'nama_lengkap', 'jenis_kelamin', 'id')
    ordering = ('nama_lengkap', 'nik')

admin.site.register(Sumber_Pendanaan)

@admin.register(Kegiatan)
class KegiatanModel(admin.ModelAdmin):
    search_fields = ('nama_kegiatan',)
    list_display = ('id', 'nama_kegiatan', 'tanggal_mulai_kegiatan', 'tanggal_selesai_kegiatan', 'sumber_pendanaan')
    list_filter = ('nama_kegiatan', 'tanggal_mulai_kegiatan', 'tanggal_selesai_kegiatan', 'sumber_pendanaan')
    raw_id_fields = ('sumber_pendanaan',)

@admin.register(Kegiatan_Petani)
class KegiatanPetaniModel(admin.ModelAdmin):
    list_display = ('id', 'id_kegiatan', 'id_petani')
    list_filter = ('id_kegiatan', 'id_petani')
    raw_id_fields = ('id_kegiatan', 'id_petani')
    ordering = ('id_kegiatan',)