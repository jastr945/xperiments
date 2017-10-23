from django.shortcuts import render
from .models import Article


# the first view: rendering the main page without any artciles
def base(request):

    context_dict = {}
    return render(request, 'searchapp/base.html', context_dict)


# rendering the main page with articles thumbnails
def index(request):

    articles = Article.objects.all().order_by('-date')

    context_dict = {
        'articles': articles,
    }
    return render(request, 'searchapp/index.html', context_dict)


# rendering a single article
def article(request, article_name_slug):

    context_dict = {}

    try:
        articles = Article.objects.get(slug=article_name_slug)
        context_dict['articles'] = articles

    except Article.DoesNotExist:
        print('Error. There is no such article.')

    return render(request, 'searchapp/article.html', context_dict)
