from django.urls import path
from . import views

app_name = "mainapp"

urlpatterns = [
    path('', views.index, name='index'),

    path('all-visas/', views.all_visas, name='all_visas'),
    path('all-visas/country/<slug:country_slug>/', views.filter_by_country, name='filter_by_country'),
    path('all-visas/category/<slug:category_slug>/', views.filter_by_category, name='filter_by_category'),
    
    path('search/', views.search_visas, name='search_visas'),

    path('about', views.about, name='about'),
    
    
    path('allcases', views.case_management, name='allcases'),
    path('api/cases/create/', views.create_case, name='create_case'),
    path("cases/<str:ref_no>/update-status/", views.update_status, name="update_status"),

    path("cases/<str:ref_no>/edit/", views.edit_case, name="edit_case"),
    path("cases/<str:ref_no>/delete/", views.delete_case, name="delete_case"),
    path('api/cases/search/', views.search_cases, name='search_cases'),
    
    path("tracking/", views.tracking, name="tracking"),
    path("track/<str:ref_no>/", views.track_case, name="track_case"),
    path("invoice/<str:ref_no>/", views.invoice_view, name="invoice_view"),
    

    path('contact', views.contact, name='contact'),
    path('countries', views.countries, name='countries'),
    path('service', views.service, name='service'),
    path('testimonial', views.testimonial, name='testimonial'),
    path('training', views.training, name='training'),


    path('help', views.help, name='help'),
    path('support', views.support, name='support'),
    path('privacy', views.privacy, name='privacy'),
    path('terms', views.terms, name='terms'),

    path('404', views.resource_not_found, name='resource_not_found'),
    path('subscribe-newsletter/', views.subscribe_newsletter, name='subscribe_newsletter'),
    path('unsubscribe-newsletter/', views.unsubscribe_newsletter, name='unsubscribe_newsletter'),


]