from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *
from django.contrib import messages
from django.db.models import Q
from django_countries.data import COUNTRIES
from django.http import JsonResponse, HttpResponse
from django.contrib.admin.views.decorators import staff_member_required
from django.views.decorators.csrf import csrf_exempt
from django.core.cache import cache
import json
from django.utils import timezone
import random
import string
import logging
from django.template.loader import render_to_string
import io
import qrcode
import base64
from django.views.decorators.cache import cache_page




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
def case_management(request):
    # Get all cases initially
    cases = Case.objects.all()
    
    # Handle search functionality
    search_query = request.GET.get('search', '')
    if search_query:
        cases = cases.filter(
            Q(ref_no__icontains=search_query) |
            Q(applicant_name__icontains=search_query) |
            Q(contact_number__icontains=search_query) |
            Q(document_type__icontains=search_query) |
            Q(agent__icontains=search_query)
        )
    
    # Handle status filtering
    status_filter = request.GET.get('status', '')
    if status_filter:
        cases = cases.filter(status=status_filter)
    
    # Handle service type filtering
    service_filter = request.GET.get('service', '')
    if service_filter:
        cases = cases.filter(service=service_filter)
    
    # Handle receiving method filtering
    receiving_method_filter = request.GET.get('receiving_method', '')
    if receiving_method_filter:
        cases = cases.filter(receiving_method=receiving_method_filter)
    
    # Get unique values for filter dropdowns
    status_choices = Case.STATUS_CHOICES
    service_choices = Case.SERVICE_CHOICES
    receiving_method_choices = Case.RECEIVING_METHOD_CHOICES
    
    context = {
        'cases': cases,
        'search_query': search_query,
        'status_filter': status_filter,
        'service_filter': service_filter,
        'receiving_method_filter': receiving_method_filter,
        'status_choices': status_choices,
        'service_choices': service_choices,
        'receiving_method_choices': receiving_method_choices,
    }
    
    return render(request, 'cases/allcases.html', context)


def tracking(request):
    return render(request, "tracking.html")


def track_case(request, ref_no):
    case = get_object_or_404(Case, ref_no=ref_no)
    # fetch history of this case
    history = case.status_history.order_by("changed_at")  
    return render(request, "tracking.html", {
        "case": case,
        "searched": True,
        "history": history
    })

# Set up logging
logger = logging.getLogger(__name__)


@staff_member_required
def create_case(request):
    if request.method == 'POST':
        try:
            logger.info("POST request received for create_case")
            logger.info(f"POST data: {dict(request.POST)}")

            form = CaseForm(request.POST)
            logger.info(f"Form is valid: {form.is_valid()}")

            if not form.is_valid():
                logger.warning(f"Form errors: {form.errors.as_json()}")
                return JsonResponse({'success': False, 'errors': form.errors})

            # Save case
            case = form.save()
            logger.info(f"Case saved successfully with ref_no: {case.ref_no}")

            # Clear cache
            cache.delete('all_cases')

            # Generate QR Code for tracking
            track_url = request.build_absolute_uri(f"/track/{case.ref_no}/")
            qr = qrcode.make(track_url)
            qr_io = io.BytesIO()
            qr.save(qr_io, format="PNG")
            qr_data = qr_io.getvalue()

            # Render invoice HTML with QR
            invoice_html = render_to_string("cases/invoice.html", {
                "case": case,
                "qr_code": qr_data.hex()  # pass hex string to template
            })

            return JsonResponse({
                'success': True,
                'ref_no': case.ref_no,
                'invoice_html': invoice_html
            })

        except Exception as e:
            logger.error(f"Error in create_case view: {str(e)}")
            return JsonResponse({'success': False, 'error': f'Server error: {str(e)}'})

    elif request.method == 'GET':
        try:
            # Generate reference number
            ref_no = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
            current_date = timezone.now().strftime('%Y-%m-%d')

            return render(request, 'cases/addcase.html', {
                'ref_no': ref_no,
                'current_date': current_date,
                'service_choices': Case.SERVICE_CHOICES,
                'receiving_method_choices': Case.RECEIVING_METHOD_CHOICES,
                'status_choices': Case.STATUS_CHOICES,
            })

        except Exception as e:
            logger.error(f"Error in GET create_case: {str(e)}")
            return JsonResponse({'success': False, 'error': str(e)})

    return JsonResponse({'success': False, 'error': 'Invalid request method'})


@staff_member_required 
def invoice_view(request, ref_no):
    """Render invoice page with QR code."""
    case = get_object_or_404(Case, ref_no=ref_no)

    # Generate QR Code
    track_url = request.build_absolute_uri(f"/track/{case.ref_no}/")
    qr = qrcode.make(track_url)
    qr_io = io.BytesIO()
    qr.save(qr_io, format="PNG")

    # ✅ Convert QR code to base64 string
    qr_base64 = base64.b64encode(qr_io.getvalue()).decode("utf-8")

    return render(request, "cases/invoice.html", {
        "case": case,
        "qr_code": qr_base64  # pass base64 instead of hex
    })


@staff_member_required
@csrf_exempt
def update_status(request, ref_no):
    if request.method == "POST":
        try:
            new_status = request.POST.get("status")
            case = get_object_or_404(Case, ref_no=ref_no)

            old_status = case.status  # keep the previous status

            # Update case
            case.status = new_status
            case.save()

            # Save to CaseStatusHistory
            CaseStatusHistory.objects.create(
                case=case,
                old_status=old_status,
                new_status=new_status
            )

            messages.success(request, f"Status updated to {new_status}.")
            return redirect("mainapp:allcases")

        except Exception as e:
            logger.error(f"Error updating status: {e}")
            messages.error(request, "Failed to update status.")
            return redirect("mainapp:allcases")


@csrf_exempt
def edit_case(request, ref_no):
    case = get_object_or_404(Case, ref_no=ref_no)

    if request.method == "POST":
        case.applicant_name = request.POST.get("applicant_name")
        case.contact_number = request.POST.get("contact_number")
        case.document_type = request.POST.get("document_type")
        case.quantity = request.POST.get("quantity") or 0
        case.service = request.POST.get("service")

        # Convert numeric fields properly
        try:
            case.rate = float(request.POST.get("rate") or 0)
        except ValueError:
            case.rate = 0

        try:
            case.advance = float(request.POST.get("advance") or 0)
        except ValueError:
            case.advance = 0

        case.receiving_method = request.POST.get("receiving_method")
        case.receiver_name = request.POST.get("receiver_name")
        case.status = request.POST.get("status")
        case.applicant_address = request.POST.get("applicant_address")
        case.agent = request.POST.get("agent")
        case.payment_received_by = request.POST.get("payment_received_by")
        case.date_created = request.POST.get("date_created")

        case.save()
        return redirect("mainapp:allcases")

    return render(request, "cases/editcase.html", {
        "case": case,
        "service_choices": Case.SERVICE_CHOICES,
        "receiving_method_choices": Case.RECEIVING_METHOD_CHOICES,
        "status_choices": Case.STATUS_CHOICES,
    })


def delete_case(request, ref_no):
    case = get_object_or_404(Case, ref_no=ref_no)
    case.delete()
    return redirect("mainapp:allcases")


def search_cases(request):
    query = request.GET.get('q', '')
    
    if query:
        # Use database indexes for fast searching
        cases = Case.objects.filter(
            Q(ref_no__icontains=query) |
            Q(applicant_name__icontains=query) |
            Q(contact_number__icontains=query)
        ).only(
            'ref_no', 'applicant_name', 'contact_number', 
            'document_type', 'quantity', 'status', 'date_created'
        )[:50]  # Limit results
        
        cases_data = [
            {
                'ref_no': case.ref_no,
                'applicant_name': case.applicant_name,
                'contact': case.contact_number,
                'doc_type': case.document_type,
                'qty': case.quantity,
                'status': case.status,
                'date': case.date_created.strftime('%m/%d/%Y')
            }
            for case in cases
        ]
        
        return JsonResponse({'cases': cases_data})
    
    return JsonResponse({'cases': []})


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
