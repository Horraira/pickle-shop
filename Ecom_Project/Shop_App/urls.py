from django.urls import path, include
from . import views
app_name = 'Shop_App'

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('product/<pk>/', views.ProductDetail.as_view(), name='product-detail'),
]