from django.contrib import admin
from .models import Category, Bundle, Addon, Image, Type


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'friendly_name',
    )


class BundleAdmin(admin.ModelAdmin):
    list_display = (
        'category',
        'bundle_slug',
        'name',
        'description',
        'price',
    )

    ordering = ('name',)


class AddonAdmin(admin.ModelAdmin):
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
admin.site.register(Bundle, BundleAdmin)
admin.site.register(Addon, AddonAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Type, TypeAdmin)
