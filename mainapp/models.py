from django.db import models
from cloudinary.models import CloudinaryField
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=50, unique=True, blank=True, null=True)
    image = CloudinaryField('image', folder='category_images')
    shortdesc = models.TextField(default="Apply Now")
    animation_delay = models.PositiveIntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ('-created',)


class Country(models.Model):
    country = CountryField(unique=True)
    slug = models.SlugField(max_length=50, unique=True, blank=True, null=True)
    famousimage = CloudinaryField('image', folder='FamousPlaces/', null=True, blank=True)
    animation_delay = models.PositiveIntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True)
    frontpage = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.country.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.country.name

    class Meta:
        verbose_name_plural = 'countries'
        ordering = ('-created',)

class Visa(models.Model):
    title = models.CharField(max_length=500, default='Visa')
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    application_process = models.TextField(blank=True, null=True)
    requirements = models.TextField(blank=True, null=True)
    processing_time = models.CharField(max_length=100, blank=True, null=True)
    fees = models.CharField(max_length=10, default='Ask Us', blank=True, null=True)
    document_upload = CloudinaryField('image', folder='visa/', null=True, blank=True)
    duration = models.CharField(max_length=100, blank=True, null=True)
    deadline = models.CharField(max_length=255, blank=True, null=True)
    appointment = models.CharField(max_length=50, choices=[('Available', 'Available'), ('Foreign', 'Foreign'), ('Paid', 'Paid')], default='Available')
    eligibility_criteria = models.TextField(blank=True, null=True)
    animation_delay = models.CharField(max_length=1, default='1', null=True, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


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
    frontpage = models.BooleanField(default=False)

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
    # Choices for the project field
    PROJECT_CHOICES = [
        ('visa', 'Visa Inquiry'),
        ('appointment', 'Appointment Request'),
        ('feedback', 'Feedback'),
        ('review', 'Review'),
        ('complaint', 'Complaint'),
        ('other', 'Other'),  # For messages that don't fit the above categories
    ]

    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True, null=True)
    project = models.CharField(
        max_length=50,
        choices=PROJECT_CHOICES,
        default='other',  # Default value to ensure database integrity
    )
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)  # Tracks if the message has been read

    def __str__(self):
        return f"{self.name} - {self.subject}"



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

    querystarter =  models.CharField(max_length=200, blank=True, null=True, help_text="Quick Contact")
    querymain =  models.CharField(max_length=200, blank=True, null=True, help_text="Have Questions? Don't Hesitate to Contact Us")
    querydesc =  models.CharField(max_length=200, blank=True, null=True, help_text="We are here to help you!")
    address =  models.CharField(max_length=200, blank=True, null=True, help_text="Office Address")
    facebook =  models.CharField(max_length=200, blank=True, null=True, help_text="http://fb.com/fviconsultants")
    tiktok =  models.CharField(max_length=200, blank=True, null=True, help_text="http://tiktok.com/fviconsultants")
    linkedin =  models.CharField(max_length=200, blank=True, null=True, help_text="http://linkedin.com/fviconsultants")
    formstarter =  models.CharField(max_length=200, blank=True, null=True, help_text="Lets Connect")
    formheading =  models.CharField(max_length=200, blank=True, null=True, help_text="Send Your Message")
    mapembedcode =  models.CharField(max_length=200, blank=True, null=True, help_text="paste embed code here")

    primary_color = models.CharField(max_length=7, default="#007bff")  # Example: Blue
    secondary_color = models.CharField(max_length=7, default="#6c757d")  # Example: Gray
    background_color = models.CharField(max_length=7, default="#ffffff")  # Example: White
    text_color = models.CharField(max_length=7, default="#000000")  # Example: Black
    
    def __str__(self):
        return self.site_title
    

class NewsletterSubscription(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
    
    