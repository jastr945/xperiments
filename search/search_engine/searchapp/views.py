from django.shortcuts import render

# rendering the main page
def index(request):

    context_dict = {
    }
    return render(request, 'searchapp/index.html', context_dict)
