"""Post Forms

Form class describes a form and determines how it works and appears.
In a similar way that a model class’s fields map to database fields,
a form class’s fields map to HTML form <input> elements.
"""

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):
    image = forms.ImageField(required=False, widget=forms.FileInput(attrs={'multiple': True}))

    class Meta:
        """Provides metadata to the ModelForm class"""
        model = Profile
        fields = ('profession', 'bio', 'image')
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4,
                                         'wrap': 'hard',
                                         'placeholder': 'Tell people something interesting about yourself!'}),
        }


class UserRegisterForm(UserCreationForm):
    email = forms.CharField(max_length=150, widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm password'}))

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')


class LoginForm(forms.Form):
    email = forms.CharField(max_length=150, widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
