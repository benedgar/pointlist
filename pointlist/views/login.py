__author__ = 'ag'

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from pointlist.forms.tools import DivErrorList
from django.views.generic import CreateView
from pointlist.views.homepage import bootstrap


from pointlist.forms.authentication import LoginForm


class Login_view(CreateView):

    form_class = LoginForm
    template_name = 'pointlist/login.html'
    success_url = "/"

    def form_invalid(self, form):
        register_form = LoginForm(self.request.POST, error_class=DivErrorList)
        return super(Login_view, self).form_invalid(register_form)

    def form_valid(self, login_form):
        """
        This method is called when valid form data has been POSTed.
        It should return an HttpResponse.
        """
        return bootstrap(self.request)

    def login(self, register_form):
        un = register_form.cleaned_data.get('username')
        pw = register_form.cleaned_data.get('password1')
        user = authenticate(username=un, password=pw)
        if user:
            login(self.request, user)


