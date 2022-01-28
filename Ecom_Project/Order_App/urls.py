from django.urls import path, include
from . import views
app_name = 'Order_App'

urlpatterns = [
    path('add/<pk>/', views.add_to_cart, name="add"),
    path('cart/', views.cart_view, name="cart"),
]