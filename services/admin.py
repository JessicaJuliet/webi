from django.contrib import admin
from .models import Category, Bundle, Addon, Image


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'friendly_name',
        'type',
    )


class BundleAdmin(admin.ModelAdmin):
    list_display = (
        # 'category',
        'name',
        'description',
        'price',
    )

    ordering = ('name',)


class AddonAdmin(admin.ModelAdmin):
    list_display = (
        # 'category',
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


# Register Models
admin.site.register(Bundle, BundleAdmin)
admin.site.register(Addon, AddonAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Category, CategoryAdmin)
