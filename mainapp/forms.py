from django import forms
from .models import *

import random
import string

class CaseForm(forms.ModelForm):
    class Meta:
        model = Case
        # Exclude auto-generated fields
        exclude = ['balance', 'expected_delivery', 'date_created', 'date_modified', 'id']
        widgets = {
            'applicant_address': forms.Textarea(attrs={'rows': 3}),
            'ref_no': forms.TextInput(attrs={'readonly': 'readonly'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Make status not required since it's auto-set
        self.fields['status'].required = False
        
        # Set initial reference number if creating new
        if not self.instance.pk:
            self.initial['ref_no'] = self.generate_reference_number()
    
    def generate_reference_number(self):
        # Generate a 10-digit unique reference number
        from django.db.models import Q
        
        while True:
            ref_no = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
            if not Case.objects.filter(ref_no=ref_no).exists():
                return ref_no
    
    def clean(self):
        cleaned_data = super().clean()
        # Remove status from cleaned_data if it's empty since it will be auto-set
        if not cleaned_data.get('status'):
            if 'status' in cleaned_data:
                del cleaned_data['status']
        return cleaned_data


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

