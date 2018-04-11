"""kubebooks URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from booksapp import views as page_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', page_views.index, name='index'),
    url(r'^main/', page_views.main, name='main'),
    url(r'^dashboard/', page_views.dashboard, name='dashboard'),
    url(r'^delete_entry/(?P<entryid>\d+)', page_views.delete_entry, name='delete_entry'),
    url(r'^', include(('django.contrib.auth.urls', 'django.contrib.auth'), namespace='auth')),
    url(r'^', include(('social_django.urls', 'social_django'), namespace='social')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
