from django.urls import path
from . import views

app_name = "mainapp"

urlpatterns = [
    path('', views.index, name='index'),

    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('countries', views.countries, name='countries'),
    path('categories', views.categories, name='categories'),
    path('service', views.service, name='service'),
    path('testimonial', views.testimonial, name='testimonial'),
    path('training', views.training, name='training'),

    path('help', views.help, name='help'),
    path('support', views.support, name='support'),
    path('privacy', views.privacy, name='privacy'),
    path('terms', views.terms, name='terms'),

    path('404', views.resource_not_found, name='resource_not_found'),


]