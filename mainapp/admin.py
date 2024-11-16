from django.contrib import admin
from .models import SiteSettings
from .models import *

# Register your models here.


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ('site_title', 'footer_text')

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation', 'rating')


@admin.register(Office)
class OfficeAdmin(admin.ModelAdmin):
    list_display = ('countryname', 'phone', 'email')



@admin.register(Country)
class MyModelAdmin(admin.ModelAdmin):
    list_display = ('get_country_name', 'get_country_code', 'frontpage')

    def get_country_name(self, obj):
        return obj.country.name  # Displays the full country name (e.g., "Canada")
    get_country_name.short_description = 'Country Name'

    def get_country_code(self, obj):
        return obj.country.code  # Displays the country code (e.g., "CA")
    get_country_code.short_description = 'Country Code'

admin.site.register(Slider)
admin.site.register(Category)
