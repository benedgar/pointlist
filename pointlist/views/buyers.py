__author__ = 'ag'
from django.shortcuts import render
from pointlist.models import Post


from pointlist.views import homepage


def boots(request):
    return render(request, 'pointlist/buyers.html',{'post_list_buy': Post.objects.filter(type_of_post=0)})