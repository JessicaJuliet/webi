from django.db import models

from django.core.validators import MinLengthValidator

from services.models import Image


class Casestudy(models.Model):
    """
    Model to display case studies
    """
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=200, unique=True)
    header_image = models.ForeignKey(
        Image, null=True, blank=True, on_delete=models.SET_NULL)
    study_subheading_1 = models.CharField(max_length=50)
    study_content_1 = models.TextField(validators=[MinLengthValidator(200)])
    study_subheading_2 = models.CharField(max_length=50)
    study_content_2 = models.TextField(validators=[MinLengthValidator(200)])
    study_subheading_3 = models.CharField(max_length=55, null=True, blank=True)
    study_content_3 = models.TextField(
        validators=[MinLengthValidator(250)], null=True, blank=True)

    def __str__(self):
        return self.title
