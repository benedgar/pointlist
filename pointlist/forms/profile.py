__author__ = 'ag'


import datetime
import re

from django.forms import ModelForm, CharField, DateField, Form, EmailField, TextInput, ChoiceField, Select, \
    BooleanField, CheckboxInput, RadioSelect
from django.forms.extras import SelectDateWidget
from django.contrib.auth import authenticate
import django.forms as forms

from pointlist.forms.tools import DateHelper, key_in_adt
from webportal.models import Person


class PersonForm(ModelForm):

    class Meta:
        model = Person
        fields = '__all__'
        exclude = ['uid', 'role']

    def __init__(self, *args, **kwargs):
        super(PersonForm, self).__init__(*args, **kwargs)


class ChangeDataForm(Form):
    first_name = CharField(max_length=100, label='First Name', widget=TextInput(
        attrs={'placeholder': 'First Name', 'class': '', 'style': ''}))
    last_name = CharField(max_length=100, label='Last Name', widget=TextInput(
        attrs={'placeholder': 'Last Name', 'class': '', 'style': ''}))