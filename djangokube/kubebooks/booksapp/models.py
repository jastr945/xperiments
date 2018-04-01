from django.db import models


class Item(models.Model):
    """Contains basic information about each book or movie."""

    itemtype = models.CharField(max_length=255, default='', null=False)
    name = models.CharField(max_length=255, default='', null=False)
    author = models.CharField(max_length=255, default='', null=False)
