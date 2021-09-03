from django.db import models
from ckeditor.fields import RichTextField


# Resource: Default text
# https://stackoverflow.com/questions/26185687/you-are-trying-to-add-a-non-nullable-field-new-field-to-userprofile-without-a
class Casestudy(models.Model):
    """
    Model to display case studies
    """
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=200, unique=True)
    image = models.ImageField(null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    featured = models.BooleanField(default=False)
    website_url = models.URLField(max_length=1024)
    github_url = models.URLField(max_length=1024)
    heading = models.CharField(max_length=200, default='Heading')
    case_study_content = RichTextField(
        default='Case study content')

    def __str__(self):
        return self.title
