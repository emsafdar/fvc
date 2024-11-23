from django.shortcuts import render, get_object_or_404
from .models import *
from .forms import *
from django.contrib import messages
from django.db.models import Q
from django_countries import countries

def index(request):
    sliders = Slider.objects.all()
    features = Feature.objects.all()
    categories = Category.objects.all()
    countries = Country.objects.filter(frontpage=True)
    ofc = Office.objects.all()
    reviews = Review.objects.all()
        # Prepare star data for each review
    for review in reviews:
        review.filled_stars = range(review.rating)  # List of filled stars
        review.empty_stars = range(5 - review.rating)  # List of empty stars
        
    return render(request, 'index.html', {'sliders': sliders,
                                          'features': features,
                                          'categories': categories,
                                          'reviews': reviews,
                                          'countries': countries,
                                          'ofc': ofc,
                                          })


def all_visas(request):
    visas = Visa.objects.all()  # Show all visas by default
    countries = Country.objects.all()
    categories = Category.objects.all()

    # Filter by country if 'country' parameter is passed in the URL
    country_slug = request.GET.get('country')
    if country_slug:
        country = get_object_or_404(Country, slug=country_slug)
        visas = visas.filter(country=country)

    # Filter by category if 'category' parameter is passed in the URL
    category_slug = request.GET.get('category')
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        visas = visas.filter(category=category)

    context = {
        'visas': visas,
        'countries': countries,
        'categories': categories,
    }
    
    return render(request, 'all_visas.html', context)

# View to filter visas by country using slug
def filter_by_country(request, country_slug):
    # Get the country object based on slug
    country = get_object_or_404(Country, slug=country_slug)
    visas = Visa.objects.filter(country=country)
    countries = Country.objects.all()
    categories = Category.objects.all()
    
    context = {
        'visas': visas,
        'countries': countries,
        'categories': categories,
        'selected_country': country,
    }
    return render(request, 'all_visas.html', context)

# View to filter visas by category using slug
def filter_by_category(request, category_slug):
    # Get the category object based on slug
    category = get_object_or_404(Category, slug=category_slug)
    visas = Visa.objects.filter(category=category)
    countries = Country.objects.all()
    categories = Category.objects.all()
    
    context = {
        'visas': visas,
        'countries': countries,
        'categories': categories,
        'selected_category': category,
    }
    return render(request, 'all_visas.html', context)

def search_visas(request):
    query = request.GET.get('q', '')  # Get the search query from the request
    results = []

    if query:
        # Match country name against the search query
        matching_country_codes = [
            code for code, name in countries if query.lower() in name.lower()
        ]

        # Perform search on title, description, category, and country
        results = Visa.objects.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(category__name__icontains=query) |  # Assuming `Category` has a `name` field
            Q(country__country__in=matching_country_codes)  # Match country codes
        ).distinct()

    context = {
        'query': query,
        'results': results,
    }
    return render(request, 'search.html', context)



def about(request):
    return render(request, 'about.html')

def contact(request):
    ofc = Office.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        project = request.POST.get('project')
        subject = request.POST.get('subject')
        message_text = request.POST.get('message')

        # Save the message to the database
        ContactMessage.objects.create(
            name=name,
            email=email,
            phone=phone,
            project=project,
            subject=subject,
            message=message_text,
        )

        # Success message for the user
        messages.success(request, "Your message has been sent successfully!")
    
    return render(request, 'contact.html', {'ofc': ofc})

def countries(request):
    countries = Country.objects.all()
    return render(request, 'countries.html', {
                                                'countries': countries,
                                            })

def service(request):
    categories = Category.objects.all()
    return render(request, 'service.html', {'categories': categories})

def testimonial(request):
    return render(request, 'testimonial.html')

def training(request):
    return render(request, 'training.html')

def help(request):
    return render(request, 'pages/help.html')

def support(request):
    return render(request, 'support.html')

def privacy(request):
    return render(request, 'privacy.html')

def terms(request):
    return render(request, 'terms.html')

def resource_not_found(request):
    return render(request, '404.html')
