from django.contrib import admin
from .models import Casestudy


class CasestudyAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'slug',
        'image',
        'image_url',
        'featured',
        'url',
        'github_url',
        'study_subheading_1',
        'study_content_1',
        'study_subheading_2',
        'study_content_2',
        'study_subheading_3',
        'study_content_3',
    )


# Register Models
admin.site.register(Casestudy, CasestudyAdmin)
