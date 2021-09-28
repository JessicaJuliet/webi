from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from services.models import Service


def bag_contents(request):

    bag_items = []
    total = 0
    service_count = 0
    bag = request.session.get('bag', {})

    for item_id, quantity in bag.items():

        service = get_object_or_404(Service, pk=item_id)
        total += quantity * service.price
        service_count += quantity
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'service': service,
        })

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        'bag_items': bag_items,
        'total': total,
        'service_count': service_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
