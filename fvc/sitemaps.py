from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from mainapp.models import *

class CategorySitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Category.objects.all()

    def lastmod(self, obj):
        return obj.created

    def location(self, obj):
        return reverse('mainapp:filter_by_category', kwargs={'category_slug': obj.slug})
    
class CountrySitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.7

    def items(self):
        return Country.objects.filter(frontpage=True)

    def lastmod(self, obj):
        return obj.created

    def location(self, obj):
        return reverse('mainapp:filter_by_country', kwargs={'country_slug': obj.slug})



class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = "weekly"

    def items(self):
        return ['mainapp:about', 'mainapp:contact']  # Add your static view names here

    def location(self, item):
        return reverse(item)

