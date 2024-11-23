from django.contrib import admin
from .models import SiteSettings
from .models import *

# Register your models here.

class VisaAdmin(admin.ModelAdmin):
    # Define the fields to display in the list view
    list_display = ('title', 'active', 'processing_time', 'fees', 'appointment')

    # Add search functionality for specific fields
    search_fields = ('title', 'country__name', 'category__name')

    # Add filters for easier navigation in the admin
    list_filter = ('appointment', 'active', 'category', 'country')

    # Add editable fields in the list view
    list_editable = ('processing_time', 'active', 'fees',  'appointment')

    # Add custom form layout in the detail view
    fieldsets = (
        (None, {
            'fields': ('title', 'country', 'category', 'description', 'application_process', 'requirements')
        }),
        ('Additional Information', {
            'fields': ('processing_time', 'fees', 'duration', 'deadline', 'appointment', 'eligibility_criteria'),
            'classes': ('collapse',),
        }),
        ('Document Upload', {
            'fields': ('document_upload',),
        }),
        ('Status', {
            'fields': ('active',),
        }),
    )

    def get_country_code(self, obj):
        return obj.country.country.code  # Displays the country code (e.g., "CA")
    get_country_code.short_description = 'Country Code'

    # Optionally you can define actions that can be performed on selected objects

admin.site.register(Visa, VisaAdmin)


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
class CountryAdmin(admin.ModelAdmin):
    list_display = ('get_country_name', 'get_country_code', 'slug', 'frontpage', 'animation_delay')
    prepopulated_fields = {'slug': ('country',)}

    def get_country_name(self, obj):
        return obj.country.name  # Displays the full country name (e.g., "Canada")
    get_country_name.short_description = 'Country Name'

    def get_country_code(self, obj):
        return obj.country.code  # Displays the country code (e.g., "CA")
    get_country_code.short_description = 'Country Code'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'animation_delay')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'email', 'subject')

admin.site.register(Feature)
admin.site.register(Training)
admin.site.register(Slider)
