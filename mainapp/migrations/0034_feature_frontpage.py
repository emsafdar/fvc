# Generated by Django 5.1.3 on 2024-11-23 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0033_contactmessage_is_read_alter_contactmessage_project_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='feature',
            name='frontpage',
            field=models.BooleanField(default=False),
        ),
    ]
