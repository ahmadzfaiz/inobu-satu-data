# Generated by Django 4.1 on 2022-09-28 04:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_article_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='year',
            field=models.SmallIntegerField(default=2022, validators=[django.core.validators.MaxValueValidator(1900), django.core.validators.MinValueValidator(2100)]),
            preserve_default=False,
        ),
    ]
