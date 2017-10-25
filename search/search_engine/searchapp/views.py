from django.shortcuts import render, HttpResponseRedirect
from .models import Article


# the first view: rendering the clear main page without any articles
def base(request):

    context_dict = {}

    if request.GET.get("category"):
        return HttpResponseRedirect('/index?category={}'.format(request.GET["category"]))

    return render(request, 'searchapp/base.html', context_dict)


# rendering the main page with articles thumbnails; if a specific category is selected, only articles from that category will be listed
def index(request):

    context_dict = {}

    articles = Article.objects.all()
    context_dict["articles"] = articles

    if request.GET.get("category"):
        articles = Article.objects.filter(category=request.GET.get("category").lower())
        context_dict["articles"] = articles

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


# rendering a search tab
def search(request):

    context_dict = {}
    return render(request, 'searchapp/search.html', context_dict)
