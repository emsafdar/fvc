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
    list_display = ('countryname', 'phone', 'email', 'location', 'animation_delay')

    # Add editable fields in the list view
    list_editable = ('phone', 'email', 'location', 'animation_delay',)


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('get_country_name', 'get_country_code', 'slug', 'frontpage', 'animation_delay')
    prepopulated_fields = {'slug': ('country',)}

    # Add editable fields in the list view
    list_editable = ('frontpage', 'animation_delay',)

    def get_country_name(self, obj):
        return obj.country.name  # Displays the full country name (e.g., "Canada")
    get_country_name.short_description = 'Country Name'

    def get_country_code(self, obj):
        return obj.country.code  # Displays the country code (e.g., "CA")
    get_country_code.short_description = 'Country Code'


@admin.register(Case)
class CaseAdmin(admin.ModelAdmin):
    list_display = ('ref_no', 'applicant_name', 'contact_number', 'document_type', 
                   'service', 'status', 'date_created')
    list_filter = ('status', 'service', 'receiving_method', 'date_created')
    search_fields = ('ref_no', 'applicant_name', 'contact_number', 'document_type')
    readonly_fields = ('date_created', 'date_modified', 'balance', 'expected_delivery')
    list_per_page = 20
    
    # Optional: Add fieldsets for better organization in the detail view
    fieldsets = (
        ('Basic Information', {
            'fields': ('ref_no', 'applicant_name', 'contact_number', 'document_type', 'quantity')
        }),
        ('Service Details', {
            'fields': ('service', 'expected_delivery', 'status')
        }),
        ('Financial Information', {
            'fields': ('rate', 'advance', 'balance')
        }),
        ('Receiving Information', {
            'fields': ('receiving_method', 'receiver_name')
        }),
        ('Additional Information', {
            'fields': ('applicant_address', 'agent', 'payment_received_by')
        }),
        ('Timestamps', {
            'fields': ('date_created', 'date_modified'),
            'classes': ('collapse',)
        }),
    )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'animation_delay')
    prepopulated_fields = {'slug': ('name',)}
    # Add editable fields in the list view
    list_editable = ('slug', 'animation_delay',)


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'is_read', 'project',)
    list_filter = ('is_read', 'created_at', 'project')
    search_fields = ('name', 'email', 'subject')
    # Add editable fields in the list view
    list_editable = ('is_read', 'project',)


@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ('title', 'tagline', 'faicon', 'frontpage', 'animationdelay',)
    search_fields = ('title',)
    # Add editable fields in the list view
    list_editable = ('tagline', 'faicon', 'frontpage', 'animationdelay',)


@admin.register(NewsletterSubscription)
class NewsletterSubscriptionAdmin(admin.ModelAdmin):
    list_display = ('email', 'subscribed_at', 'is_subscribed',)
    search_fields = ('email',)
    list_filter = ('subscribed_at',)
    list_editable = ('is_subscribed',)


admin.site.register(Training)



@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'tagline', 'calltoaction', 'actionurl', 'active',)
    list_editable = ('title', 'tagline', 'calltoaction', 'actionurl', 'active',)

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset

