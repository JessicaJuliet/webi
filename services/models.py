from django.db import models
from ckeditor.fields import RichTextField


class Type(models.Model):
    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name


class Category(models.Model):
    """
    Category model to filter services by type
    """
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Bundle(models.Model):
    """
    Bundles model to display bundles information
    """
    category = models.ForeignKey(
        'category', null=True, blank=True, on_delete=models.SET_NULL)
    bundle_slug = models.SlugField(max_length=200, unique=True, default="bundle slug")
    name = models.CharField(max_length=254)
    description = RichTextField()
    image = models.ForeignKey(
        'Image', null=True, blank=True, on_delete=models.SET_NULL)
    addon = models.ManyToManyField('Addon')
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name


class Addon(models.Model):
    """
    Addons model to display add-ons information
    """
    category = models.ForeignKey(
        'category', null=True, blank=True, on_delete=models.SET_NULL)
    type = models.ForeignKey(
        'Type', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    description = RichTextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ForeignKey(
        'Image', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class Image(models.Model):
    """
    Images model to display services images
    """
    name = models.CharField(max_length=254)
    image = models.ImageField(null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)

    def __str__(self):
        return self.name
