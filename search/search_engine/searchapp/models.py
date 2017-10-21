from django.db import models


def upload_image(instance, filename):
    """Images will be uploaded to MEDIA_ROOT/<name>/<filename>"""

    return '{title}/{filename}'.format(title=instance.title, filename=filename)


class Article(models.Model):
    """Contains basic information about each article."""

    title = models.CharField(max_length=255, default='', null=True)
    body = models.CharField(max_length=3000, default='', null=True)
    date = models.DateField(blank=False, null=False)
    source = models.CharField(max_length=255, default='', null=True)
    img = models.FileField(upload_to=upload_image)
