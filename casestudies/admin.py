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
        'case_study_content'
    )


# Register Models
admin.site.register(Casestudy, CasestudyAdmin)
