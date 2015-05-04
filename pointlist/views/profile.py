__author__ = 'ag'

from django.shortcuts import render
from django.views.generic import UpdateView
from pointlist.models import Person
from pointlist.views import homepage

def profileView(request):
    template = 'pointlist/profile.html'

    return render(request, 'pointlist/profile.html', {'user': homepage.bootstrap})
