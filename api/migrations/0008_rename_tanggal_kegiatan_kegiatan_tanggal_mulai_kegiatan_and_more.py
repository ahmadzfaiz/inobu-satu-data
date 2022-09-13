# Generated by Django 4.1 on 2022-09-13 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_kegiatan_sumber_pendanaan'),
    ]

    operations = [
        migrations.RenameField(
            model_name='kegiatan',
            old_name='tanggal_kegiatan',
            new_name='tanggal_mulai_kegiatan',
        ),
        migrations.AddField(
            model_name='kegiatan',
            name='tanggal_selesai_kegiatan',
            field=models.DateField(default='1/1/1900'),
        ),
    ]
