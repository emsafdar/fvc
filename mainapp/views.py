from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *
from django.contrib import messages
from django.db.models import Q
from django_countries.data import COUNTRIES
from django.http import HttpResponse
from django.contrib.admin.views.decorators import staff_member_required



def index(request):
    sliders = Slider.objects.filter(active=True)
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
    query = request.GET.get('q', '').strip()  # Get the search query and clean it
    results = []

    if query:
        # COUNTRIES is a dictionary-like object
        matching_country_codes = [
            code for code, name in COUNTRIES.items() if query.lower() in name.lower()
        ]

        # Perform search on Visa model
        results = Visa.objects.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(category__name__icontains=query) |  # Assuming category is related properly
            Q(country__country__in=matching_country_codes)  # Match by country codes
        ).distinct()

    context = {
        'query': query,
        'results': results,
    }
    return render(request, 'search.html', context)


def about(request):
    return render(request, 'about.html')


def contact(request):
    ofc = Office.objects.all()  # If unrelated, this can be removed
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save the data from the form to the database
            ContactMessage.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                phone=form.cleaned_data['phone'],
                project=form.cleaned_data['project'],
                subject=form.cleaned_data['subject'],
                message=form.cleaned_data['message'],
            )
            messages.success(request, "Your message has been sent successfully!")
        else:
            messages.error(request, "Please correct the errors below.")

    return render(request, 'contact.html', {'form': form, 'ofc': ofc})

def countries(request):
    countries = Country.objects.all()
    return render(request, 'countries.html', {
                                                'countries': countries,
                                            })
@staff_member_required
def allcases(request):
    countries = Country.objects.all()
    return render(request, 'cases.html', {
                                                'countries': countries,
                                            })

def tracking(request):
    countries = Country.objects.all()
    return render(request, 'tracking.html', {
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

def subscribe_newsletter(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            subscription, created = NewsletterSubscription.objects.get_or_create(email=email)

            if created or not subscription.is_subscribed:
                subscription.is_subscribed = True
                subscription.save()
                messages.success(request, "You have successfully subscribed to our newsletter!")
            else:
                unsubscribe_url = reverse('mainapp:unsubscribe_newsletter')
                messages.info(request, f"You are already subscribed. <a href='{unsubscribe_url}'>Click here to unsubscribe</a>", extra_tags='safe')
        else:
            messages.error(request, "Please enter a valid email address.")
    return redirect('mainapp:index')  # Adjust redirect to the appropriate page


def unsubscribe_newsletter(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            try:
                subscription = NewsletterSubscription.objects.get(email=email)
                if subscription.is_subscribed:
                    subscription.is_subscribed = False
                    subscription.save()
                    messages.success(request, "You have successfully unsubscribed from our newsletter.")
                else:
                    messages.info(request, "You are already unsubscribed.")
            except NewsletterSubscription.DoesNotExist:
                messages.error(request, "This email is not subscribed.")
        else:
            messages.error(request, "Please enter a valid email address.")
    return redirect('mainapp:index')  # Adjust redirect to the appropriate page



def robots_txt(request):
    lines = [
        "User-agent: *",
        "Disallow: /admin/",
        "Allow: /",
        "Sitemap: https://www.fviconsultants.com/sitemap.xml",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")
