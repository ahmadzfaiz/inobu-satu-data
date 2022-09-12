# Generated by Django 4.1 on 2022-09-05 07:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('operation', '0005_catalog_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalog',
            name='category',
            field=models.CharField(choices=[('JSON', 'JavaScript Object Notation (JSON)'), ('XML', 'Extensible Markup Language (XML)'), ('WFS', 'Web Feature Service (WFS)'), ('WMS', 'Web Map Service (WMS)'), ('WMTS', 'Web Map Tile Service (WMTS)'), ('XYZ', 'XYZ Tile Layer')], default='JSON', max_length=50),
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('category', models.CharField(choices=[('document', 'Document format (.doc)'), ('spreadsheet', 'Spreadsheet format (.xls)'), ('presentation', 'Presentation format (.ppt)'), ('portable', 'Portable document format (.pdf)')], default='document', max_length=50)),
                ('url', models.URLField(unique=True)),
                ('description', models.TextField()),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('published', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('tags', models.ManyToManyField(to='operation.tag')),
            ],
        ),
    ]