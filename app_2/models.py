from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType

# Create your models here.

class Model1(models.Model):

    fchar = models.CharField(max_length=100)
    fdate = models.DateField(blank=True, null=True)
    fdatetime = models.DateTimeField(auto_now_add=True)
    fbool = models.BooleanField()
    fdeci = models.DecimalField(decimal_places=2, max_digits=6)
    fint = models.IntegerField()
    furl = models.URLField()


class Model2(models.Model):
    f2char = models.CharField(max_length=100)
    f2date = models.DateField(blank=True, null=True)
    f2datetime = models.DateTimeField(auto_now_add=True)
    f2bool = models.BooleanField()
    f2deci = models.DecimalField(decimal_places=2, max_digits=6)
    f2int = models.IntegerField()
    f2url = models.URLField()

