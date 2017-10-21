from django.shortcuts import render
from .models import Article

# rendering the main page
def index(request):

    articles = Article.objects.all()

    context_dict = {
        'articles': articles,
    }
    return render(request, 'searchapp/index.html', context_dict)
