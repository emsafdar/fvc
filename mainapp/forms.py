from django import forms
from .models import *


class ContactForm(forms.Form):
    PROJECT_CHOICES = [
        ('visa', 'Visa Inquiry'),
        ('appointment', 'Appointment Request'),
        ('feedback', 'Feedback'),
        ('review', 'Review'),
        ('complaint', 'Complaint'),
        ('other', 'Other'),
    ]

    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Your Name', 'id': 'name'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control', 'placeholder': 'Your Email', 'id': 'email'
    }))
    phone = forms.CharField(max_length=15, widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Your Phone', 'id': 'phone'
    }))
    project = forms.ChoiceField(choices=PROJECT_CHOICES, widget=forms.Select(attrs={
        'class': 'form-control', 'id': 'project'
    }))
    subject = forms.CharField(max_length=150, widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Subject', 'id': 'subject'
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control', 'placeholder': 'Leave a message here', 'id': 'message', 'style': 'height: 160px'
    }))


class NewsletterForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control border-0 rounded-pill w-100 py-3 ps-4 pe-5',
        'placeholder': 'Enter your email'
    }))

