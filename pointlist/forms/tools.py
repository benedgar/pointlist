__author__ = 'ag'

import datetime
from django.forms.util import ErrorList


class DivErrorList(ErrorList):
    def __unicode__(self):
        return self.as_divs()

    def as_divs(self):
        if not self:
            return u''
        return u'<div class="errorlist">%s</div>' % ''.join([u'<div class="bg-danger">%s</div>' % e for e in self])


def key_in_adt(key, adt):
    return key in adt

class DateHelper:
    today = datetime.date.today()

    def __init__(self):
        pass

    @staticmethod
    def get_year():
        return DateHelper.today.year