from django.shortcuts import render
from django.http import HttpResponse
# from . import models
from .models import Verbit


# Create your views here.


def i1(request):
    w = Verbit.objects.all()
    return render(request, 'mystock/page1.html', {'w': w})  # главная


def index(request):
    return HttpResponse("Hello from mystock")  # /myst


def i2(request):
    return render(request, 'mystock/page2.html')  # /myst/
