from django.shortcuts import redirect, render
from lists.models import Item

def home_page(request):
    if request.method == 'POST': 
        Item.objects.create(text=request.POST['item_text'])     # .objects.create is short for creating and saving new Item     = ... get the POST parameter (new to-do item)
        return redirect('/')

    return render(request, 'home.html')     # render takes the HttpRequest as its first parameter, and the name of the template to render (will search in 'templates' folder) and
                                            #   builds an HttpResponse based on the content of the template

