from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from django.contrib import messages
from Order_App.models import Order

# Create your views here.


@login_required
def checkout(request):
    saved_address = BillingAddress.objects.get_or_create(user=request.user)[0]
    form = BillingForm(instance=saved_address)
    if request.method == 'POST':
        form = BillingForm(request.POST, instance=saved_address)
        if form.is_valid():
            form.save()
            form = BillingForm(instance=saved_address)
            messages.success(request, f"Shipping address saved.")
    return render(request, 'Payment_App/checkout.html', context={"form": form})