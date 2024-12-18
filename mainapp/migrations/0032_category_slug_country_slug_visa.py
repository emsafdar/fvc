# Generated by Django 5.1.3 on 2024-11-22 21:38

import cloudinary.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0031_alter_category_shortdesc'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='country',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
        migrations.CreateModel(
            name='Visa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Visa', max_length=500)),
                ('description', models.TextField(blank=True, null=True)),
                ('application_process', models.TextField(blank=True, null=True)),
                ('requirements', models.TextField(blank=True, null=True)),
                ('processing_time', models.CharField(blank=True, max_length=100, null=True)),
                ('fees', models.CharField(blank=True, default='Visa', max_length=500, null=True)),
                ('document_upload', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image')),
                ('duration', models.CharField(blank=True, max_length=100, null=True)),
                ('deadline', models.CharField(blank=True, max_length=255, null=True)),
                ('appointment', models.CharField(choices=[('Available', 'Available'), ('Foreign', 'Foreign'), ('Paid', 'Paid')], default='Available', max_length=50)),
                ('eligibility_criteria', models.TextField(blank=True, null=True)),
                ('active', models.BooleanField(default=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.category')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.country')),
            ],
        ),
    ]
