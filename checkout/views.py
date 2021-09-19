from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('addons'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key':
        'pk_test_51JQzAWHai2DHN8peN5ULHBcoyqvIE5mOdxljvVP01RgbARUL2VkIbKjKXaD9nRZDAgUsiyNKGSIh19Z9OyIW8sob006iKfbVM9',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
