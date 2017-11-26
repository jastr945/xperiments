from django.db import models
from django.template.defaultfilters import slugify


def upload_image(instance, filename):
    """Images will be uploaded to MEDIA_ROOT/<name>/<filename>"""

    return '{title}/{filename}'.format(title=instance.title, filename=filename)


class Article(models.Model):
    """Contains basic information about each article."""

    title = models.CharField(max_length=255, default='', null=True)
    body = models.TextField(max_length=100000, default='', null=True)
    date = models.DateField(blank=False, null=False)
    author = models.CharField(max_length=255, default='', null=True)
    source = models.CharField(max_length=255, default='', null=True)
    img = models.FileField(upload_to=upload_image, default='', blank=True, null=True)
    slug = models.SlugField(max_length=200, default='', unique=True)

    CATEGORY_CHOICES = (
        ('blog posts', 'blog posts'),
        ('articles', 'articles'),
        ('poems', 'poems')
    )

    category = models.FileField(max_length=50, choices=CATEGORY_CHOICES, default='', blank=True)

    def __str__(self):
        return '{} - {}'.format(self.title, self.category)

    def save(self, *args, **kwargs):
        """the slug will change every time the article's title changes"""
        self.slug = slugify(self.title)
        super(Article, self).save(*args, **kwargs)
