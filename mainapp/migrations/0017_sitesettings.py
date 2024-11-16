# Generated by Django 5.1.3 on 2024-11-16 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0016_office_animation_delay'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_title', models.CharField(help_text='The title of your site', max_length=200)),
                ('logo', models.ImageField(blank=True, help_text='Upload the site logo', null=True, upload_to='logos/')),
                ('footer_text', models.CharField(blank=True, help_text='Footer text for the site', max_length=500, null=True)),
            ],
        ),
    ]
