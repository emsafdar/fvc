from django.shortcuts import render
from .models import *
from .forms import *
from django.contrib import messages


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
