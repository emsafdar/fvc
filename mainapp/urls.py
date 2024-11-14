from django.urls import path
from . import views

app_name = "mainapp"

urlpatterns = [
    path('', views.index, name='index'),
    path('product/<pk>/', views.ProductDetail.as_view(), name='product_detail'),

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

    path('add/<pk>', views.add_to_cart, name='add'),
    path('cart/', views.cart_view, name='cart'),
    path('remove/<pk>', views.remove_from_cart, name='remove'),

    path('signup/', views.sign_up, name='signup'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/', views.user_profile, name='profile'),

    #path('checkout/', views.checkout, name='checkout'),
    #path('pay/', views.payment, name='payment'),
    #path('status/', views.complete, name='complete'),
    #path('purchase/<val_id>/<tran_id>/', views.purchased, name='purchase'),
    #path('order/', views.order_view, name='orders'),

]