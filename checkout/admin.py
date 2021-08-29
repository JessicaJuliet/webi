from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fileds = ('order_numer', 'date',
                       'order_total', 'grand_total')

    fields = ('order_number', 'date', 'full_name', 'email', 'phone_number',
              'country', 'postcode', 'town_or_city', 'street_address',
              'county', 'order_total', 'grand_total',)

    list_display = ('order_number', 'date', 'full_name',
                    'order_total', 'grand_total',)

    ordering = ('-date',)

admin.site.register(Order, OrderAdmin)
