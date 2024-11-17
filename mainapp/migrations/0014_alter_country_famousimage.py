# Generated by Django 5.1.3 on 2024-11-16 15:03

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0013_country_frontpage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='famousimage',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
    ]