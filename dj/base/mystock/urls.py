
from django.urls import path
from .views import *
from mystock.views import i2

urlpatterns = [

    path('', index),         # /myst/
    path('/2', i2, name='p2'),       # /myst/2

]
