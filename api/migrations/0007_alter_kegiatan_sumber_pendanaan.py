# Generated by Django 4.1 on 2022-09-13 03:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_kegiatan_sumber_pendanaan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kegiatan',
            name='sumber_pendanaan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.sumber_pendanaan'),
        ),
    ]
