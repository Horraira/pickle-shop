from django.shortcuts import render
from .models import *

from django.views.generic import ListView, DetailView
# Create your views here.


class Home(ListView):
    model = Product
    template_name = 'Shop_App/home.html'
