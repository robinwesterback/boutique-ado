from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51HjVihGzTE5Kpg61pU4Wy2EsmF5jMXfHCaAMkQRaYaxXK0dR6xYGLncOOSYEtbrJduvaesrgUH6zNW6qKoE0y7QY00p16sRT7Y',
        'client_secret':  'test client secret',
    }

    return render(request, template, context)
