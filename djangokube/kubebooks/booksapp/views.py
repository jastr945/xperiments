from django.shortcuts import render
from .models import Item

def index(request):
    try:
        items = Item.objects.all()
        if request.POST:
            new_itemtype=request.POST['itemtype']
            new_title=request.POST['title']
            new_author=request.POST['author']
            item_instance = Item(itemtype=new_itemtype, title=new_title, author=new_author)
            item_instance.save()
    except ValueError:
        pass
    return render(request, 'booksapp/index.html', {"items": items})
