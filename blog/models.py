from django.db import models
from django.core.validators import MinLengthValidator
# from services.models import Image
from ckeditor.fields import RichTextField


class Blog(models.Model):
    """
    Model to display Blog
    """
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=200, unique=True)
    blog_content = RichTextField()

    def __str__(self):
        return self.title
