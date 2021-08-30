from django.contrib import admin
from .models import Blog


class BlogAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'slug',
        # 'header_image',
        'blog_subheading_1',
        'blog_content_1',
        'blog_subheading_2',
        'blog_content_2',
        'blog_subheading_3',
        'blog_content_3',
    )


# Register Models
admin.site.register(Blog, BlogAdmin)
