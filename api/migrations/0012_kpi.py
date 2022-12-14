# Generated by Django 4.1 on 2022-09-15 12:37

import django.core.validators
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_remove_kegiatan_kpi_delete_kpi'),
    ]

    operations = [
        migrations.CreateModel(
            name='KPI',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nama_kpi', models.CharField(max_length=100)),
                ('tahun_kpi', models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(9999)])),
            ],
            options={
                'verbose_name': 'Key Performance Indicator',
                'ordering': ('nama_kpi',),
            },
        ),
    ]
