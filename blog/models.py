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
    blog_image = models.ImageField(null=True, blank=True)
    # blog_image = models.ForeignKey(
    #    'Image', null=True, blank=True, on_delete=models.SET_NULL)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    blog_content = RichTextField(default='Blog content goes here')

    def __str__(self):
        return self.title
