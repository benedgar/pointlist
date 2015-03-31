__author__ = 'ag'

from django.contrib.auth import authenticate, login
from django.views.generic import CreateView
from webportal.forms.tools import DivErrorList
from webportal.forms.register import SignUpForm


class SignUpView(CreateView):
    """
    This the view for handling the user sign up page.
    """
    form_class = SignUpForm
    template_name = 'pointcoin/signup.html'
    success_url = "/pointcoin/profile#update_information"

    def form_invalid(self, form):
        register_form = SignUpForm(self.request.POST, error_class=DivErrorList)
        return super(SignUpView, self).form_invalid(register_form)

    def form_valid(self, register_form):
        """
        This method is called when valid form data has been POSTed.
        It should return an HttpResponse.
        """
        register_form.save()
        self.login(register_form)
        self.send_registration_email(register_form)
        return super(SignUpView, self).form_valid(register_form)

    def login(self, register_form):
        un = register_form.cleaned_data.get('username')
        pw = register_form.cleaned_data.get('pwdFirstTry')
        user = authenticate(username=un, password=pw)
        if user:
            login(self.request, user)

    @staticmethod
    def send_registration_email(form):
        user_email = form.cleaned_data.get('email')
        to = [user_email]
        subject = "Thank you for registering!"
        body = "User,\n\nThank you for registering with us!"
        # TODO: commented out temporarily; preventing spam email
        # Emailer().send_email(to, subject, body)