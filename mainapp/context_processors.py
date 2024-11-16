from .models import SiteSettings

def site_settings(request):
    try:
        settings = SiteSettings.objects.first()  # Retrieve the first (or only) settings instance
        if settings:  # Ensure settings is not None
            return {
                'site_title': settings.site_title,
                'logo': settings.logo.url if settings.logo else None,
                'footer_text': settings.footer_text,
                'contact_desc': settings.contact_desc,
            }
        else:
            # Return default settings if no SiteSettings exists
            return {
                'site_title': 'Default Site Title',
                'logo': None,
                'footer_text': 'Default footer text',
                'contact_desc': 'Default contact desc',
            }
    except SiteSettings.DoesNotExist:
        return {
            'site_title': 'Default Site Title',
            'logo': None,
            'footer_text': 'Default footer text',
            'contact_desc': 'Default contact desc',
        }

