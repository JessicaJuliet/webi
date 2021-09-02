from django.db import models
from django.core.validators import MinLengthValidator
from services.models import Image
from ckeditor.fields import RichTextField


class Casestudy(models.Model):
    """
    Model to display case studies
    """
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=200, unique=True)
    image = models.ImageField(null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    featured = models.BooleanField(default=False)
    url = models.URLField(max_length=1024)
    github_url = models.URLField(max_length=1024)
    case_study_content = RichTextField()

    def __str__(self):
        return self.title
