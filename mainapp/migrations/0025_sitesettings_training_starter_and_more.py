# Generated by Django 5.1.3 on 2024-11-17 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0024_sitesettings_reviews_starter_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesettings',
            name='training_starter',
            field=models.CharField(blank=True, help_text='CHECK OUR TRAINING', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='sitesettings',
            name='trainingdesc',
            field=models.CharField(blank=True, help_text='Training from Our experts', max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='sitesettings',
            name='trainingmain',
            field=models.CharField(blank=True, help_text='Best Coacing Service', max_length=200, null=True),
        ),
    ]