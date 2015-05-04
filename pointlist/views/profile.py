from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from pointlist.pointcoin_tools import check_balance, update_last_balance, spend

__author__ = 'ag'

from pointlist.models import PointcoinAddress
from django.shortcuts import render
from django.views.generic import UpdateView
from pointlist.models import Person
from pointlist.views import homepage

def profileView(request):
    template = 'pointlist/profile.html'
    addr = PointcoinAddress.objects.get(uid=request.user)
    update_last_balance(addr.address)
    return render(request, 'pointlist/profile.html', {'username': request.user,
                                                      'balance': addr.current_amount,
                                                      'address': addr.address})


@login_required
def parse_ajax(request):
    """
    Parse the ajax request for spending pointcoin
    """
    return parse_ajax_helper(request.GET, request.user)


def parse_ajax_helper(get, user):
    try:
        if 'spend' in get and 'amount' in get and 'toAddress' in get:
            addr = PointcoinAddress.objects.get(uid=user)
            flag = spend(get['amount'], get['toAddress'], addr.address)
            if flag:
                return HttpResponse("SPENT")
            else:
                return HttpResponse("ERROR_SPENDING")
        elif 'store' in get:
            print 'in store yo'
            addr = PointcoinAddress.objects.get(uid=user)
            curr_bal = check_balance(addr.address)
            if curr_bal > addr.last_balance:
                print 'balance changed'
                addr.current_amount = curr_bal - addr.last_balance
                addr.last_balance = curr_bal
                addr.save()
                return HttpResponse("CHANGED")
            else:
                print 'balanced not changed'
                return HttpResponse("NOT_CHANGED")
        else:
            return HttpResponse("BAD")
    except Exception as e:
        return HttpResponse("BAD %s" % e)
    return HttpResponse("OK")
