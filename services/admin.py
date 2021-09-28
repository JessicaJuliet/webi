from django.contrib import admin
from .models import Category, Service, Image, Type


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'friendly_name',
    )


class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        'category',
        'type',
        'name',
        'description',
        'price',
    )

    ordering = ('name',)


class ImageAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'image',
        'image_url',
    )

    ordering = ('name',)


class TypeAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


# Register Models
admin.site.register(Image, ImageAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(Service, ServiceAdmin)
