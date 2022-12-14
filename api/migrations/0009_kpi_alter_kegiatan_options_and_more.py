# Generated by Django 4.1 on 2022-09-15 11:08

import django.core.validators
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_rename_tanggal_kegiatan_kegiatan_tanggal_mulai_kegiatan_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='KPI',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nama_kpi', models.CharField(max_length=20)),
                ('tahun_kpi', models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(9999)])),
            ],
            options={
                'verbose_name': 'Key Performance Indicator',
                'ordering': ('nama_kpi',),
            },
        ),
        migrations.AlterModelOptions(
            name='kegiatan',
            options={'ordering': ('nama_kegiatan',), 'verbose_name': 'Kegiatan', 'verbose_name_plural': 'Kegiatan'},
        ),
        migrations.AlterField(
            model_name='kegiatan',
            name='tanggal_selesai_kegiatan',
            field=models.DateField(),
        ),
        migrations.AddField(
            model_name='kegiatan',
            name='kpi',
            field=models.ManyToManyField(to='api.kpi'),
        ),
    ]
