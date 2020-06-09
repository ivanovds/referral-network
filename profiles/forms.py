"""Profile Forms

Form class describes a form and determines how it works and appears.
In a similar way that a model class’s fields map to database fields,
a form class’s fields map to HTML form <input> elements.
"""

from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):
    image = forms.ImageField(required=False, widget=forms.FileInput(attrs={'multiple': True}))

    class Meta:
        model = Profile
        fields = ('profession', 'bio', 'image')
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4,
                                         'wrap': 'hard',
                                         'placeholder': 'Tell people something interesting about yourself!'}),
        }
