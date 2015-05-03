__author__ = 'ag'
from django.shortcuts import render
from pointlist.models import Post


from pointlist.views import homepage


def boots(request):
    return render(request, 'pointlist/sellers.html',{'post_list_sell': Post.objects.filter(type_of_post=1)})