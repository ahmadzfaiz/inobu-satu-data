from django.db import models
import uuid

class Article(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=30)
    description = models.TextField()

    def __str__(self):
        return self.title

class Petani(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    nik = models.CharField(max_length=16, unique=True)
    gelar_depan = models.CharField(max_length=50, blank=True)
    nama_lengkap = models.CharField(max_length=100, blank=True)
    gelar_belakang = models.CharField(max_length=50, blank=True)
    jenis_kelamin = models.CharField(max_length=10, choices=[('Laki-laki', 'Laki-laki'), ('Perempuan', 'Perempuan')], blank=True)
    desa = models.CharField(max_length=50, blank=True)
    kecamatan = models.CharField(max_length=50, blank=True)
    kabupaten = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.nama_lengkap
    
    def save(self, *args, **kwargs):
        self.nama_lengkap = self.nama_lengkap.upper()
        self.desa = self.desa.upper()
        self.kecamatan = self.kecamatan.upper()
        self.kabupaten = self.kabupaten.upper()
        return super(Petani, self).save(*args, **kwargs)