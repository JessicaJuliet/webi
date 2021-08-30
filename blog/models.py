from django.db import models

from django.core.validators import MinLengthValidator

from services.models import Image


class Blog(models.Model):
    """
    Model to display Blog
    """
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=200, unique=True)
    header_image = models.ForeignKey(
        Image, null=True, blank=True, on_delete=models.SET_NULL)
    blog_subheading_1 = models.CharField(max_length=50)
    blog_content_1 = models.TextField(validators=[MinLengthValidator(200)])
    blog_subheading_2 = models.CharField(max_length=50)
    blog_content_2 = models.TextField(validators=[MinLengthValidator(200)])
    blog_subheading_3 = models.CharField(max_length=55, null=True, blank=True)
    blog_content_3 = models.TextField(
        validators=[MinLengthValidator(250)], null=True, blank=True)

    def __str__(self):
        return self.title
