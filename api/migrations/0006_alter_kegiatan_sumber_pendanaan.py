# Generated by Django 4.1 on 2022-09-12 12:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_kegiatan_petani'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kegiatan',
            name='sumber_pendanaan',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='api.sumber_pendanaan'),
        ),
    ]