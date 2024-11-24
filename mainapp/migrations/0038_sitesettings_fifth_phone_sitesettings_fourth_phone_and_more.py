# Generated by Django 5.1.3 on 2024-11-24 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0037_newslettersubscription_is_subscribed'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesettings',
            name='fifth_phone',
            field=models.CharField(default='+923215258534', max_length=200),
        ),
        migrations.AddField(
            model_name='sitesettings',
            name='fourth_phone',
            field=models.CharField(default='+923316000300', max_length=200),
        ),
        migrations.AddField(
            model_name='sitesettings',
            name='metadescription',
            field=models.TextField(blank=True, default='visa consultant', null=True),
        ),
        migrations.AddField(
            model_name='sitesettings',
            name='metakeywords',
            field=models.TextField(blank=True, default='visa', null=True),
        ),
        migrations.AddField(
            model_name='sitesettings',
            name='third_phone',
            field=models.CharField(default='+923046578001', max_length=200),
        ),
        migrations.AddField(
            model_name='sitesettings',
            name='uk_phone',
            field=models.CharField(default='+44 xxx', max_length=200),
        ),
        migrations.AddField(
            model_name='sitesettings',
            name='us_phone',
            field=models.CharField(default='+1 xxxx', max_length=200),
        ),
        migrations.AlterField(
            model_name='sitesettings',
            name='phone_primary',
            field=models.CharField(default='+923021108001', max_length=200),
        ),
        migrations.AlterField(
            model_name='sitesettings',
            name='phone_secondary',
            field=models.CharField(default='+923017978598', max_length=200),
        ),
    ]