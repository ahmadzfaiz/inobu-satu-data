from django.db import models
import uuid
import datetime

class Article(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=30)
    description = models.TextField()

    def __str__(self):
        return self.title

class Petani(models.Model):
    class Meta:
        verbose_name = 'Petani'
        verbose_name_plural = 'Petani'

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

class Sumber_Pendanaan(models.Model):
    class Meta:
        verbose_name = 'Sumber Pendanaan'
        verbose_name_plural = 'Sumber Pendanaan'
    
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    nama_donor =  models.CharField(max_length=50)

    def __str__(self):
        return self.nama_donor
    
    def save(self, *args, **kwargs):
        self.nama_donor = self.nama_donor.upper()
        return super(Sumber_Pendanaan, self).save(*args, **kwargs)

class Kegiatan(models.Model):
    class Meta:
        verbose_name = 'Kegiatan'
        verbose_name_plural = 'Kegiatan'

    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    nama_kegiatan = models.CharField(max_length=100)
    tanggal_mulai_kegiatan = models.DateField()
    tanggal_selesai_kegiatan = models.DateField()
    sumber_pendanaan = models.ForeignKey('Sumber_Pendanaan',on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self):
        return self.nama_kegiatan

    def save(self, *args, **kwargs):
        self.nama_kegiatan = self.nama_kegiatan.upper()
        return super(Kegiatan, self).save(*args, **kwargs)

class Kegiatan_Petani(models.Model):
    class Meta:
        verbose_name = 'Kegiatan Petani'
        verbose_name_plural = 'Kegiatan Petani'
    
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    id_kegiatan = models.ForeignKey('Kegiatan', on_delete=models.CASCADE)
    id_petani = models.ForeignKey('Petani', on_delete=models.CASCADE)

    def __str__(self):
        return self.id