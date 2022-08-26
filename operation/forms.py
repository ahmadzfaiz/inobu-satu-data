from xml.dom import ValidationErr
from django import forms
from django.contrib.auth.models import User
from .models import Catalog

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class UserRegistration(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', )

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Password dont match')

        return cd['password2']

class CatalogInsertForm(forms.ModelForm):
    class Meta:
        model = Catalog
        fields = ('title', 'url', 'description')