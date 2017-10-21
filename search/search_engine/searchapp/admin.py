from django.contrib import admin
from django.db import models
from .models import Article
from django.forms import TextInput


class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '200'})},
    }

admin.site.register(Article, ArticleAdmin)
