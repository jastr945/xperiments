from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from .models import Article
from .documents import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import json
from django.contrib import messages


# the first view: rendering the clear main page without any articles
def start(request):

    context_dict = {}

    if request.GET.get("category"):
        return HttpResponseRedirect('/index?category={}'.format((request.GET["category"]).lower()))

    return render(request, 'searchapp/start.html', context_dict)


# rendering the main page with articles thumbnails; articles can be filtered by category; 10 articles per page is displayed
def index(request):

    articles = Article.objects.all()
    paginator = Paginator(articles, 10) # Show 10 articles per page
    page = request.GET.get('page')

    try:
        articles = paginator.page(page)

    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        articles = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        articles = paginator.page(paginator.num_pages)

    if request.GET.get("category"):

        articles = Article.objects.filter(category=request.GET.get("category").lower())
        paginator = Paginator(articles, 10) # Show 10 articles per page
        page = request.GET.get('page')

        try:
            articles = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            articles = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            articles = paginator.page(paginator.num_pages)


    return render(request, 'searchapp/index.html', {'articles': articles})


# rendering a single article
def article(request, article_name_slug):

    context_dict = {}

    if request.GET.get("category"):
        return HttpResponseRedirect('/index?category={}'.format((request.GET["category"]).lower()))

    try:
        articles = Article.objects.get(slug=article_name_slug)
        context_dict['articles'] = articles

    except Article.DoesNotExist:
        messages.error(request, "Oops! There is no such article in the database.")

    return render(request, 'searchapp/article.html', context_dict)


# rendering a search tab
def search(request):

    context_dict = {}

    if request.GET.get("category"):
        return HttpResponseRedirect('/index?category={}'.format((request.GET["category"]).lower()))

    if request.POST:
        s = ArticleDocument.search().query("query_string", query=request.POST["srchterm"] + "~1")
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
