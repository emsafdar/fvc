from django.db import models
from cloudinary.models import CloudinaryField
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField

class Category(models.Model):
    name = models.CharField(max_length=100)
    image = CloudinaryField('image', folder='category_images')
    shortdesc = models.CharField(max_length=1000, default="Apply Now")
    animation_delay = models.PositiveIntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ('-created',)


class Review(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    photo = CloudinaryField('image', folder='testimonial_images')
    review_msg = models.CharField(max_length=1000, default="Apply Now")
    rating = models.IntegerField(default=0)
    animation_delay = models.PositiveIntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'reviews'
        ordering = ('-created',)


class Country(models.Model):
    country = CountryField()
    famousimage = CloudinaryField('image', folder='FamousPlaces/', null=True, blank=True)
    animation_delay = models.PositiveIntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True)
    frontpage = models.BooleanField(default=False)

    def __str__(self):
        return self.country.name

    class Meta:
        verbose_name_plural = 'countries'
        ordering = ('-created',)

class Office(models.Model):
    officeimg = CloudinaryField('image', folder='about/', null=True, blank=True)
    countryname = CountryField()
    phone = models.CharField(max_length=100)
    email  = models.EmailField()
    location = models.CharField(max_length=100)
    animation_delay = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.countryname.name

    class Meta:
        verbose_name_plural = 'Offices'


class SiteSettings(models.Model):
    site_title = models.CharField(max_length=200, help_text="The title of your site")
    logo =  CloudinaryField('image', folder='about/', help_text="Upload the site logo", null=True, blank=True)
    footer_text = models.CharField(max_length=500, blank=True, null=True, help_text="Footer text for the site")
    contact_desc = models.CharField(max_length=1000, null=True, blank=True)
    
    def __str__(self):
        return self.site_title

class Slider(models.Model):
    title  = models.CharField(max_length=200, help_text="starting single line 200ch")
    tagline = models.CharField(max_length=200, help_text="h1 big font 200ch")
    desc = models.CharField(max_length=500, help_text="test under heading 500ch")
    headerimg = CloudinaryField('image', folder='sliders')

    def __str__(self):
        return self.title

