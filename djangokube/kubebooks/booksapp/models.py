from django.db import models


class Item(models.Model):
    """Contains basic information about each book or movie."""

    itemtype = models.CharField(max_length=255, default='', null=False)
    title = models.CharField(max_length=255, default='', null=False)
    author = models.CharField(max_length=255, default='', null=False)

    def save(self, *args, **kwargs):
        """Saving an Item instance in the database"""
        super(Item, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        """Deleting an Item instance from the database"""
        super(Item, self).delete(*args, **kwargs)
