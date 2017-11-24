from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
    return render(request, 'home.html', {       # render takes the HttpRequest as its first parameter, and the name of the template to render (will search in 'templates' folder) and
                                                #   builds an HttpResponse based on the content of the template
        'new_item_text': request.POST.get('item_text', ''),     # this line pass the POST parameter to the template
                                                                # .get() returns the value for 'item_text' if its in the dictionary, else default ('')

    })
