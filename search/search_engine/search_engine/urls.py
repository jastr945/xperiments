"""search_engine URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from searchapp import views as page_views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include

app_name = 'searchapp'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', page_views.start, name='start'),
    url(r'^index/', page_views.index, name='index'),
    url(r'^search/', page_views.search, name='search'),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^get_titles/', page_views.get_titles, name='get_titles'),
    url(r'^texts/(?P<article_name_slug>[-\w]+)/$', page_views.article, name='article'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
