# Create your views here.To make your project available on the web.
# we need to configure url routing
# to direct web request to the correct views.

from django.shortcuts import render
from django.http import HttpResponse
from .models import Snippet

def snippet_list(request):
    """ A view to display a list of code snippets """
    snippets = Snippet.objects.all()
    # snippets_list = ','.join([snippet.title for snippet in snippets])
    # render function takes: 
        # request object, 
        # path to the template, 
        # context dictionary as an argument
    # then generates dynamic HTML page as response.
    return render(request, 'snippets/snippet_list.html', {'snippets': snippets})
    # return HttpResponse(f'List of Snippets: {snippets_list}')