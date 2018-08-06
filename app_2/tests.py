
from .models import (
    Model1,
    Model2,
)

from datetime import datetime

# Create your tests here.

from datetime import datetime


def populate1():
    for i in range(1, 100):
        m1 = Model1()
        m1.fchar = 'dino{}'.format(i)
        m1.fdate = datetime(2018 + i, 1, 1)
        m1.fbool = i % 2
        m1.fdeci = i
        m1.fint = i
        m1.furl = 'http://www.example.com/{}'.format(i)

        m1.save()


def populate2():
    for i in range(11, 200):
        m1 = Model2()
        m1.f2char = 'dino2{}'.format(i)
        m1.f2date = datetime(2018 + i, 2, 2)
        m1.f2bool = i % 2
        m1.f2deci = i
        m1.f2int = i
        m1.f2url = 'http://www.example2.com/{}'.format(i)

        m1.save()
