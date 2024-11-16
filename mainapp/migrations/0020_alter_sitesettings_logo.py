# Generated by Django 5.1.3 on 2024-11-16 19:34

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0019_slider'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitesettings',
            name='logo',
            field=cloudinary.models.CloudinaryField(blank=True, help_text='Upload the site logo', max_length=255, null=True, verbose_name='image'),
        ),
    ]
