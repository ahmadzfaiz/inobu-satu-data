# Generated by Django 4.1 on 2022-09-12 12:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_sumber_pendanaan_alter_petani_desa_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='kegiatan',
            options={'verbose_name': 'Kegiatan', 'verbose_name_plural': 'Kegiatan'},
        ),
        migrations.AlterModelOptions(
            name='petani',
            options={'verbose_name': 'Petani', 'verbose_name_plural': 'Petani'},
        ),
        migrations.AlterModelOptions(
            name='sumber_pendanaan',
            options={'verbose_name': 'Sumber Pendanaan', 'verbose_name_plural': 'Sumber Pendanaan'},
        ),
        migrations.RemoveField(
            model_name='kegiatan',
            name='tahun_kegiatan',
        ),
    ]
