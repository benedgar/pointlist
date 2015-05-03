from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

TYPE_OF_POST_CHOICES = ((0, 'Buyer'), (1, 'Seller'))

class Person(models.Model):
    uid = models.OneToOneField(User)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    bio = models.CharField(max_length=200)
    pointcoin_public_address = models.CharField(max_length=50)


    def __init__(self, *args, **kwargs):
        super(Person, self).__init__(*args, **kwargs)
        self.__i = -1
        self.__cols = ['id', 'uid', 'first_name', 'last_name']

    def __iter__(self):
        return self

    def next(self):
        if self.__i < len(self.__cols) - 1:
            self.__i += 1
            return self.__cols[self.__i]
        else:
            raise StopIteration


class PointcoinAddress(models.Model):
    uid = models.ForeignKey(User)
    address = models.CharField(max_length=34)
    current_amount = models.IntegerField()
    last_balance = models.IntegerField()


class Post(models.Model):
    uid = models.ForeignKey(User)
    date = models.DateField()
    name = models.CharField(max_length=140)
    description = models.CharField(max_length=500)
    price = models.IntegerField()
    public_address = models.CharField(max_length=34)
    type_of_post = models.IntegerField(choices=TYPE_OF_POST_CHOICES)
