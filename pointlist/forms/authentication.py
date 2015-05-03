__author__ = 'ag'

from django.contrib.auth import authenticate
from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm


class LoginForm(ModelForm):
    """
    This is for user authentication. Logout is handled by django auth.
    """
    username = forms.CharField(label="",
                               widget=forms.TextInput(
                                   attrs={'placeholder': 'Username', 'class': 'form-control'}),
                               required=True)
    password = forms.CharField(label="",
                               widget=forms.PasswordInput(
                                   attrs={'placeholder': 'Password', 'class': 'form-control'}),
                               required=True)

    def clean(self):
        un = self.cleaned_data.get('username')
        pw = self.cleaned_data.get('password')
        usr = authenticate(username=un, password=pw)
        if not usr or not usr.is_active:
            self.fields['username'].widget = forms.TextInput(
            attrs={'class': 'form-control', 'id': 'inputError2'})
            raise forms.ValidationError("Login was invalid. Please try again.")
        return self.cleaned_data

    def login(self, request):
        un = self.cleaned_data.get('username')
        pw = self.cleaned_data.get('password')
        usr = authenticate(username=un, password=pw)
        return usr

    class Meta:
        model = User
        fields = ("username", "password")