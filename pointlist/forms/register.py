__author__ = 'ag'

from django import forms
from django.forms import CharField
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from webportal.forms.tools import DivErrorList, key_in_adt


class SignUpForm(UserCreationForm):

    username = forms.RegexField(label="Username", max_length=30,
                                regex=r'^[\w.@+-]+$',
                                error_messages={'invalid': "This value may contain only letters, numbers and @/./+/-/_"
                                                           " characters."},
                                widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'}))
    pwdFirstTry = CharField(label="Password",
                          widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control'}))
    pwdSecondTry = CharField(label="Password Confirmation",
                          widget=forms.PasswordInput(
                              attrs={'placeholder': 'Confirm Password', 'class': 'form-control'}))

    def clean_username(self):
        # Since User.username is unique, this check is redundant,
        # but it sets a nicer error message than the ORM. See #13147.
        cd = self.cleaned_data
        username = cd["username"]
        try:
            User._default_manager.get(username=username)
        except User.DoesNotExist:
            return username
        msg = "Username already exists"
        self.fields['username'].widget = forms.TextInput(
            attrs={'placeholder': msg, 'class': 'form-control', 'id': 'inputError2'})
        # raise forms.ValidationError(
        # self.error_messages['duplicate_username'],
        # code='duplicate_username',
        # )

    def clean(self):
        cd = self.cleaned_data
        pw1 = cd.get('pwdFirstTry')
        err_bool = False

        if not pw1:
            msg = "Password cannot be blank"
            err_bool = True
        else:
            if len(pw1) < 7:
                msg = "Password requires 7+ characters"
                err_bool = True
            elif 'pwdSecondTry' in self.errors:
                msg = "Passwords do not match"
                err_bool = True

        if err_bool:
            self._errors['pwdFirstTry'] = self.error_class([msg])
            if key_in_adt("pwdFirstTry", cd):
                del cd["pwdFirstTry"]
            self.fields['pwdFirstTry'].widget = forms.PasswordInput(
                attrs={'placeholder': msg, 'class': 'form-control', 'id': 'inputError2'})

        return cd

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email")
        widgets = {"email": forms.TextInput(attrs={'placeholder': 'email address', 'class': 'form-control'})}

    def __init__(self, *args, **kwargs):
        kwargs_new = {'error_class': DivErrorList}
        kwargs_new.update(kwargs)
        super(SignUpForm, self).__init__(*args, **kwargs_new)


