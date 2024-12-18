# Generated by Django 5.1.3 on 2024-11-17 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0028_contactmessage'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesettings',
            name='address',
            field=models.CharField(blank=True, help_text='Office Address', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='sitesettings',
            name='facebook',
            field=models.CharField(blank=True, help_text='http://fb.com/fviconsultants', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='sitesettings',
            name='formheading',
            field=models.CharField(blank=True, help_text='Send Your Message', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='sitesettings',
            name='formstarter',
            field=models.CharField(blank=True, help_text='Lets Connect', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='sitesettings',
            name='linkedin',
            field=models.CharField(blank=True, help_text='http://linkedin.com/fviconsultants', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='sitesettings',
            name='mapembedcode',
            field=models.CharField(blank=True, help_text='paste embed code here', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='sitesettings',
            name='querydesc',
            field=models.CharField(blank=True, help_text='We are here to help you!', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='sitesettings',
            name='querymain',
            field=models.CharField(blank=True, help_text="Have Questions? Don't Hesitate to Contact Us", max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='sitesettings',
            name='querystarter',
            field=models.CharField(blank=True, help_text='Quick Contact', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='sitesettings',
            name='tiktok',
            field=models.CharField(blank=True, help_text='http://tiktok.com/fviconsultants', max_length=200, null=True),
        ),
    ]
