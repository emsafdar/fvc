# Generated by Django 5.1.3 on 2024-11-24 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0034_feature_frontpage'),
    ]

    operations = [
        migrations.AddField(
            model_name='visa',
            name='animation_delay',
            field=models.CharField(blank=True, default='1', max_length=1, null=True),
        ),
    ]
