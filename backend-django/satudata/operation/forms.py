from django import forms
from .models import Catalog

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class CatalogInsertForm(forms.ModelForm):
    class Meta:
        model = Catalog
        fields = ('title'  'url'  'description')