# Generated by Django 5.1.3 on 2024-11-15 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='shortdesc',
            field=models.CharField(default='Apply Now', max_length=1000),
        ),
    ]
