"""
Definition of forms.
"""
from django import forms
from django.db import models
from .models import MyModel
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _

COLOR_CHOICES = (
    ('green','GREEN'),
    ('blue', 'BLUE'),
    ('red','RED'),
    ('orange','ORANGE'),
    ('black','BLACK'),
)

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))
    dob = forms.DateField(label=_("DateofBirth"),
                               widget=forms.DateInput({
                                   'class': 'form-control',
                                   'placeholder':'Date of Birth'}))
    days = forms.ChoiceField(choices=[(x, x) for x in range(1, 32)])

    color = forms.ChoiceField(choices=COLOR_CHOICES,required=True)
     