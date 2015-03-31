from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    uid = models.OneToOneField(User)
    date = models.DateField()
    name = models.CharField(max_length=140)
    description = models.CharField(max_length=500)
    public_address = models.CharField(max_length=34)
    '''doc string'''



