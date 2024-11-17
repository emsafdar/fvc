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
    phone_primary = models.CharField(max_length=200, help_text="+923021108001")
    phone_secondary = models.CharField(max_length=200, help_text="+923017978598")
    email = models.CharField(max_length=200, help_text="fviconsultants@gmail.com")

    countries_starter =  models.CharField(max_length=200, blank=True, null=True, help_text="Countries we offer")
    countries_main =  models.CharField(max_length=200, blank=True, null=True, help_text="Immigration & visa services following Countries")
    countries_desc =  models.CharField(max_length=500, blank=True, null=True, help_text="Visa Services accross the globe")

    chooseus_starter =  models.CharField(max_length=200, blank=True, null=True, help_text="why choose us")
    chooseus_main =  models.CharField(max_length=200, blank=True, null=True, help_text="Services That Our Client Requires")
    chooseus_desc =  models.CharField(max_length=500, blank=True, null=True, help_text="Visa Services accross the globe")

    reviews_starter =  models.CharField(max_length=200, blank=True, null=True, help_text="OUR CLIENTS REVIEWS")
    reviewsmain =  models.CharField(max_length=200, blank=True, null=True, help_text="What Our Clients Say")
    reviewsdesc =  models.CharField(max_length=500, blank=True, null=True, help_text="reviews desc")

    training_starter =  models.CharField(max_length=200, blank=True, null=True, help_text="CHECK OUR TRAINING")
    trainingmain =  models.CharField(max_length=200, blank=True, null=True, help_text="Best Coacing Service")
    trainingdesc =  models.CharField(max_length=500, blank=True, null=True, help_text="Training from Our experts")

    office_starter =  models.CharField(max_length=200, blank=True, null=True, help_text="Worlwide Offices")
    officemain =  models.CharField(max_length=200, blank=True, null=True, help_text="Explore Our Office Worldwide")
    officedesc =  models.CharField(max_length=500, blank=True, null=True, help_text="somewhat about our worldwide offices")

    primary_color = models.CharField(max_length=7, default="#007bff")  # Example: Blue
    secondary_color = models.CharField(max_length=7, default="#6c757d")  # Example: Gray
    background_color = models.CharField(max_length=7, default="#ffffff")  # Example: White
    text_color = models.CharField(max_length=7, default="#000000")  # Example: Black
    
    def __str__(self):
        return self.site_title
    


class Slider(models.Model):
    title  = models.CharField(max_length=200, help_text="starting single line 200ch")
    tagline = models.CharField(null=True, blank=True, max_length=200, help_text="h1 big font 200ch")
    desc = models.CharField(null=True, blank=True, max_length=500, help_text="test under heading 500ch")
    headerimg = CloudinaryField('image', folder='sliders')

    def __str__(self):
        return self.title

class Feature(models.Model):
    title  = models.CharField(max_length=200, help_text="name of feature")
    tagline = models.CharField(null=True, blank=True, max_length=200, help_text="some words about the feature")
    desc = models.TextField(null=True, blank=True, help_text="Details of the feature")
    faicon = models.CharField(max_length=50, null=True, blank=True)
    animationdelay = models.CharField(max_length=1, null=True, blank=True)

    def __str__(self):
        return self.title

class Training(models.Model):
    title  = models.CharField(max_length=200, help_text="name of feature")
    tagline = models.CharField(null=True, blank=True, max_length=200, help_text="some words about the feature")
    desc = models.TextField(null=True, blank=True, help_text="Details of the feature")
    image = CloudinaryField('image', folder='trainings')
    animationdelay = models.CharField(max_length=1, null=True, blank=True)

    def __str__(self):
        return self.title

class ContactMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True, null=True)
    project = models.CharField(max_length=255, blank=True, null=True)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"

