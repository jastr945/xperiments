from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Item
from django.contrib.auth.decorators import login_required
import json


def index(request):
    """Redirecting to dashboard if the user is authorized."""
    if request.user.is_anonymous == True:
        return redirect('main')
    else:
        return redirect('dashboard')
    return HttpResponse("OK")

def main(request):
    """Invitation to log in."""
    return render(request, 'booksapp/authorize.html', {})

@login_required
def dashboard(request):
    """Displaying a Wishlist of an authenticated user."""
    context_dict = {}
    user = request.user
    auth0user = user.social_auth.get(provider="auth0")
    userdata = {
    'user_id': auth0user.uid,
    'name': user.first_name,
    'picture': auth0user.extra_data['picture']
    }
    context_dict["userdata"] = json.dumps(userdata, indent=4)
    context_dict["auth0User"] = auth0user
    try:
        items = Item.objects.filter(user=auth0user.uid)
        context_dict["items"] = items
        if request.POST:
            new_itemtype = request.POST['itemtype']
            new_title = request.POST['title']
            new_author = request.POST['author']
            belongs_to = auth0user.uid
            item_instance = Item(itemtype=new_itemtype, title=new_title, author=new_author, user=belongs_to)
            item_instance.save()
    except ValueError:
        pass
    return render(request, 'booksapp/dashboard.html', context_dict)

@login_required
def delete_entry(request, entryid):
    """Deleting a single entry from the list."""
    get_object_or_404(Item, id=entryid).delete()
    return HttpResponse("deleted")
