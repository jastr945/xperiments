from django.contrib import admin
from django.db import models
from .models import Article
from django.forms import TextInput
from tinymce.widgets import TinyMCE


class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '200'})},
        models.TextField: {'widget': TinyMCE(attrs={'cols': 20, 'rows': 100}, )},
    }

admin.site.register(Article, ArticleAdmin)
