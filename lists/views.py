from django.shortcuts import render
from lists.models import Item

def home_page(request):
    if request.method == 'POST':
        new_item_text = request.POST['item_text']   # get the POST parameter (new to-do item)
        Item.objects.create(text=new_item_text)     # .objects.create is short for creating new Item, without needing to call .save()
    else:
        new_item_text = ''

    return render(request, 'home.html', {       # render takes the HttpRequest as its first parameter, and the name of the template to render (will search in 'templates' folder) and
                                                #   builds an HttpResponse based on the content of the template
        'new_item_text': new_item_text,         # pass POST parameter to template
    })
