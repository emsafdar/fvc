from django.forms import ModelForm
from django import forms
from .models import *

from django.contrib.auth.forms import UserCreationForm

#UserProfileForm
class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ('user',)

#SignUpForm
class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email','password1','password2',)

class BillingForm(forms.ModelForm):
    class Meta:
        model = BillingAddress
        fields = ['email', 'address', 'zipcode', 'city', 'country']

