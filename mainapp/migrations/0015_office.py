# Generated by Django 5.1.3 on 2024-11-16 15:29

import cloudinary.models
import django_countries.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0014_alter_country_famousimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('officeimg', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image')),
                ('countryname', django_countries.fields.CountryField(max_length=2)),
                ('phone', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('location', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Offices',
            },
        ),
    ]