from .models import SiteSettings

def site_settings(request):
    try:
        settings = SiteSettings.objects.first()  # Retrieve the first (or only) settings instance
        if settings:  # Ensure settings is not None
            return {
                'site_title': settings.site_title,
                'logo': settings.logo.url if settings.logo else None,
                'footer_text': settings.footer_text,

                'phone_primary': settings.phone_primary,
                'phone_secondary': settings.phone_secondary,
                'email': settings.email,

                'office_starter': settings.office_starter,
                'officemain': settings.officemain,
                'officedesc': settings.officedesc,

                'countries_starter': settings.countries_starter,
                'countries_main': settings.countries_main,
                'countries_desc': settings.countries_desc,

                'chooseus_starter': settings.chooseus_starter,
                'chooseus_main': settings.chooseus_main,
                'chooseus_desc': settings.chooseus_desc,

                'reviews_starter':  settings.reviews_starter,
                'reviewsmain':  settings.reviewsmain,
                'reviewsdesc':  settings.reviewsdesc,
            
                'training_starter':  settings.training_starter,
                'trainingmain':  settings.trainingmain,
                'trainingdesc':  settings.trainingdesc,

                'querystarter': settings.querystarter,
                'querymain': settings.querymain,
                'querydesc': settings.querydesc,
                'address': settings.address,
                'facebook': settings.facebook,
                'tiktok': settings.tiktok,
                'linkedin': settings.linkedin,
                'formstarter': settings.formstarter,
                'formheading': settings.formheading,
                'mapembedcode': settings.mapembedcode,

                'primary_color': settings.primary_color,
                'secondary_color': settings.secondary_color,
                'background_color': settings.background_color,
                'text_color': settings.text_color,
            }
        else:
            # Return default settings if no SiteSettings exists
            return {
                'site_title': 'Default Site Title',
                'logo': None,
                'footer_text': 'Default footer text',

                'phone_primary': "+923021108001",
                'phone_secondary': "+923017978598",
                'email': "fviconsultants@gmail.com",

                'office_starter': "Worlwide Offices",
                'officemain': "Explore Our Office Worldwide",
                'officedesc': "Visa Services accross the globe",

                'countries_starter': "Countries we offer",
                'countries_main': "Immigration & visa services following Countries",
                'countries_desc': "Visa Services accross the globe",

                'chooseus_starter': "why choose us",
                'chooseus_main': "Services That Our Client Requires",
                'chooseus_desc': "Visa Services accross the globe",

                'reviews_starter':  "OUR CLIENTS REVIEWS",
                'reviewsmain':  "What Our Clients Say",
                'reviewsdesc':  "reviews desc",
            
                'training_starter':  "CHECK OUR TRAINING",
                'trainingmain':  "Best Coacing Service",
                'trainingdesc':  "Training from Our experts",

                'querystarter': "Quick Contact",
                'querymain': "Have Questions? Don't Hesitate to Contact Us",
                'querydesc': "We are here to help you!",
                'address': "Office Address",
                'facebook': "http://fb.com/fviconsultants",
                'tiktok': "http://tiktok.com/fviconsultants",
                'linkedin': "http://linkedin.com/fviconsultants",
                'formstarter': "Let’s Connect",
                'formheading': "Send Your Message",
                'mapembedcode': "paste embed code here",

                'primary_color': 'Default primary color',
                'secondary_color': 'Default secondary_color',
                'background_color': 'Default background_color',
                'text_color': 'Default text_color',
            }
    except SiteSettings.DoesNotExist:
        return {
            'site_title': 'Default Site Title',
            'logo': None,
            'footer_text': 'Default footer text',

            'phone_primary': "+923021108001",
            'phone_secondary': "+923017978598",
            'email': "fviconsultants@gmail.com",

            'office_starter': "Worlwide Offices",
            'officemain': "Explore Our Office Worldwide",
            'officedesc': "Visa Services accross the globe",

            'countries_starter': "Countries we offer",
            'countries_main': "Immigration & visa services following Countries",
            'countries_desc': "Visa Services accross the globe",

            'chooseus_starter': "why choose us",
            'chooseus_main': "Services That Our Client Requires",
            'chooseus_desc': "Visa Services accross the globe",

            'reviews_starter':  "OUR CLIENTS REVIEWS",
            'reviewsmain':  "What Our Clients Say",
            'reviewsdesc':  "reviews desc",
            
            'training_starter':  "CHECK OUR TRAINING",
            'trainingmain':  "Best Coacing Service",
            'trainingdesc':  "Training from Our experts",

            'querystarter': "Quick Contact",
            'querymain': "Have Questions? Don't Hesitate to Contact Us",
            'querydesc': "We are here to help you!",
            'address': "Office Address",
            'facebook': "http://fb.com/fviconsultants",
            'tiktok': "http://tiktok.com/fviconsultants",
            'linkedin': "http://linkedin.com/fviconsultants",
            'formstarter': "Let’s Connect",
            'formheading': "Send Your Message",
            'mapembedcode': "paste embed code here",

            'primary_color': 'Default primary color',
            'secondary_color': 'Default secondary_color',
            'background_color': 'Default background_color',
            'text_color': 'Default text_color',
        }

