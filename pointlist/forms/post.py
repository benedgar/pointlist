__author__ = 'ag'

import datetime
from django.forms import ModelForm, CharField, TextInput, DateField, Select, IntegerField
from django.forms.extras import SelectDateWidget
from pointlist.models import Post
from webportal.forms.tools import DivErrorList

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['name', 'description', 'public_address', 'type_of_post']

    this_year = datetime.date.today().year
    name = CharField(max_length=140, label='Post Title', required=True, widget=TextInput(
        attrs={'placeholder': 'Title', 'class': 'form-control'}
    ))
    description = CharField(max_length=500, label='Description', required=True,
                            widget=TextInput(attrs={'placeholder': 'Description', 'class': 'form-control'}))
    public_address = CharField(max_length=34, label='Public Address', required=True,
                               widget=TextInput(attrs={'placeholder': 'Public Address', 'class': 'form-control'}))
    TYPE_OF_POST_CHOICES = ((0, 'Buyer'), (1, 'Seller'))
    type_of_post = IntegerField(label='Buyer or Seller?', required=True,
                                widget=Select(choices=TYPE_OF_POST_CHOICES,
                                              attrs={'class': 'selector form-control',
                                                     'style': ''}))

    # def __init__(self, uid=None, *args, **kwargs):
    #     self.uid = uid
    #     kwargs_new = {'error_class': DivErrorList}
    #     kwargs_new.update(kwargs)
    #     super(PostForm, self).__init__(*args, **kwargs_new)


