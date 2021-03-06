__author__ = 'ag'
"""
TODO: Licence, Authors, Date
"""

from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from pointlist.forms.register import SignUpForm
from pointlist.models import Post


def add_to_context(request, key, context):
    if key in request.session:
        context[key] = request.session[key]
        return 1
    return 0


def bootstrap(request):
    # form = LoginForm(request.POST or None)
    form = SignUpForm


    context = {#'login_form': form,
               'post_list_buy': Post.objects.filter(type_of_post=0),
               'post_list_sell': Post.objects.filter(type_of_post=1),
               'user': request.user,
               'text': {'title': 'Test', 'button_name': 'Button Text'},
               }
    return render(request, 'pointlist/index.html', context)
