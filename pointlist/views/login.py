__author__ = 'ag'

from django.shortcuts import render
from pointlist.views.homepage import bootstrap
from django.contrib.auth import login
from pointlist.forms.authentication import LoginForm


def login_view(request):
    form = LoginForm(request.POST or None)
    if request.GET:
        return render(request, 'pointlist/login.html', {'form': form})
    elif request.POST and form.is_valid():
        user = form.login(request)
        if user:
            user.is_active = True
            user.save()
            login(request, user)
            return bootstrap(request)
    return render(request, 'pointlist/login.html', {'form': form})