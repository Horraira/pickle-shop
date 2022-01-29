from django.urls import path, include
from . import views
app_name = 'Payment_App'

urlpatterns = [
    path('checkout/', views.checkout, name="checkout"),
]