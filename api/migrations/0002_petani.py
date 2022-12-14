# Generated by Django 4.1 on 2022-09-12 02:43

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Petani',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nik', models.CharField(max_length=16)),
                ('gelar_depan', models.CharField(max_length=50)),
                ('nama_lengkap', models.CharField(max_length=100)),
                ('gelar_belakang', models.CharField(max_length=50)),
                ('jenis_kelamin', models.CharField(choices=[('Laki-laki', 'Laki-laki'), ('Perempuan', 'Perempuan')], max_length=10)),
                ('desa', models.CharField(max_length=50)),
                ('kecamatan', models.CharField(max_length=50)),
                ('kabupaten', models.CharField(max_length=50)),
            ],
        ),
    ]
