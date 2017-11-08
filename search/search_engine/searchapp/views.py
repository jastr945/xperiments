from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from .models import Article
from .documents import *
import json
from django.contrib import messages


# the first view: rendering the clear main page without any articles
def start(request):

    context_dict = {}

    if request.GET.get("category"):
        return HttpResponseRedirect('/index?category={}'.format(request.GET["category"]))

    return render(request, 'searchapp/start.html', context_dict)


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

    if request.GET.get("category"):
        return HttpResponseRedirect('/index?category={}'.format(request.GET["category"]))

    try:
        articles = Article.objects.get(slug=article_name_slug)
        context_dict['articles'] = articles

    except Article.DoesNotExist:
        print('Error. There is no such article.')

    return render(request, 'searchapp/article.html', context_dict)


# rendering a search tab
def search(request):

    context_dict = {}

    if request.GET.get("category"):
        return HttpResponseRedirect('/index?category={}'.format(request.GET["category"]))

    if request.POST:
        s = ArticleDocument.search().query("common", _all=request.POST["srchterm"] + "*")
        qs = s.to_queryset()
        if qs.exists():
            context_dict['qs'] = qs
        else:
            messages.error(request, "No matching results found.")

    return render(request, 'searchapp/search.html', context_dict)


# passing titles to JQuery autocomplete
def get_titles(request):
    q = request.GET.get('term')
    articles = Article.objects.filter(title__icontains=q, author__icontains=q)
    results = []
    for a in articles:
        results.append(a.title)
        results.append(a.author)
    return HttpResponse(json.dumps(results),'application/json')
