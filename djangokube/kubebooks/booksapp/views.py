from django.shortcuts import render
from .models import Item

def index(request):
    try:
        items = Item.objects.all()
        if request.POST:
            itemtype=request.POST['itemtype']
            title=request.POST['title']
            author=request.POST['author']
            import ipdb; ipdb.set_trace()
    except ValueError:
        pass
    return render(request, 'booksapp/index.html', {"items": items})
