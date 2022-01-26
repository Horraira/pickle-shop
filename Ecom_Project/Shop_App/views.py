from django.shortcuts import render
from .models import *

# import views
from django.views.generic import ListView, DetailView

# import mixins
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class Home(ListView):
    model = Product
    template_name = 'Shop_App/home.html'


class ProductDetail(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'Shop_App/product_detail.html'
