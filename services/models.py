from django.db import models


class Category(models.Model):
    """
    Category model to filter services by type
    """
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    type = models.ForeignKey(
        'Type', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Bundle(models.Model):
    """
    Bundles model to display bundles information
    """
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    # addon = models.ForeignKey('Addon', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class Type(models.Model):
    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name


class Addon(models.Model):
    """
    Addons model to display add-ons information
    """
    category = models.ForeignKey(
        'Type', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

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
