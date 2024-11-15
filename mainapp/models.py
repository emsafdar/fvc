from django.db import models
from cloudinary.models import CloudinaryField
from django.utils.translation import gettext_lazy as _



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

