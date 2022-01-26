from django.urls import path, include
from . import views
app_name = 'Shop_App'

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
]