"""Post Forms

Form class describes a form and determines how it works and appears.
In a similar way that a model class’s fields map to database fields,
a form class’s fields map to HTML form <input> elements.
"""

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):

    class Meta:
        """Provides metadata to the ModelForm class"""
        model = Profile
        fields = ('profession', 'bio', 'image')
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4,
                                         'placeholder': 'Tell people something interesting about yourself!'}),
        }

    # def clean_title(self):
    #     """Validates title field"""
    #     data = self.cleaned_data['title']
    #     if :
    #         raise forms.ValidationError("")
    #
    #     # Always return a value to use as the new cleaned data, even if
    #     # this method didn't change it.
    #     return data


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm password'}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))