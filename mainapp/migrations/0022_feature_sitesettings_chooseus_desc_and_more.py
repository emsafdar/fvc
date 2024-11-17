# Generated by Django 5.1.3 on 2024-11-17 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0021_sitesettings_background_color_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='name of feature', max_length=200)),
                ('tagline', models.CharField(help_text='some words about the feature', max_length=200)),
                ('desc', models.TextField(help_text='Details of the feature')),
                ('faicon', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='sitesettings',
            name='chooseus_desc',
            field=models.CharField(blank=True, help_text='Visa Services accross the globe', max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='sitesettings',
            name='chooseus_main',
            field=models.CharField(blank=True, help_text='Services That Our Client Requires', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='sitesettings',
            name='chooseus_starter',
            field=models.CharField(blank=True, help_text='why choose us', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='sitesettings',
            name='countries_desc',
            field=models.CharField(blank=True, help_text='Visa Services accross the globe', max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='sitesettings',
            name='countries_main',
            field=models.CharField(blank=True, help_text='Immigration & visa services following Countries', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='sitesettings',
            name='countries_starter',
            field=models.CharField(blank=True, help_text='Countries we offer', max_length=200, null=True),
        ),
    ]
