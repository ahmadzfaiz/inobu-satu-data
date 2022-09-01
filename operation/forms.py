from django import forms
from django.contrib.auth.models import User
from .models import Catalog, Tag, Dashboard

# BASIC FORMS
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

# CATALOG RESTAPI FORMS
class CatalogInsertForm(forms.ModelForm):
    class Meta:
        model = Catalog
        fields = ('title', 'tags', 'url', 'description')

class CatalogUpdateForm(forms.ModelForm):
    class Meta:
        model = Catalog
        fields = ('title', 'tags', 'url', 'description')

class CatalogInsertTag(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ('name',)

# PRODUCT DASHBOARD FORMS
class DashboardInsertForm(forms.ModelForm):
    class Meta:
        model = Dashboard
        fields = ('title', 'tags', 'url', 'description')

class DashboardUpdateForm(forms.ModelForm):
    class Meta:
        model = Dashboard
        fields = ('title', 'tags', 'url', 'description')