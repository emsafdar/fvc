# Generated by Django 5.1.3 on 2024-11-16 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0012_alter_country_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='frontpage',
            field=models.BooleanField(default=False),
        ),
    ]
