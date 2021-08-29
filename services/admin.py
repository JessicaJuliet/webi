from django.contrib import admin
from .models import Bundle, Addon, Image, Category

# Register your models here.
admin.site.register(Bundle)
admin.site.register(Addon)
admin.site.register(Image)
admin.site.register(Category)
