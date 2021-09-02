from django.contrib import admin
from .models import Blog


class BlogAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'slug',
        # 'header_image',
        'blog_content'
    )


# Register Models
admin.site.register(Blog, BlogAdmin)
