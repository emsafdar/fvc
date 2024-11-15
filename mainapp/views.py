from django.shortcuts import render
from .models import *
from .forms import *


def index(request):
    categories = Category.objects.all()
    return render(request, 'index.html', {'categories': categories})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def countries(request):
    return render(request, 'countries.html')

def categories(request):
    return render(request, 'categories.html')

def service(request):
    return render(request, 'service.html')

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
