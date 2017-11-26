from django.shortcuts import redirect, render
from lists.models import Item

def home_page(request):
    return render(request, 'home.html')

def view_list(request):
    items = Item.objects.all()
    return render(request, 'list.html', {'items': items})       # render takes the HttpRequest as its first parameter, and the name of the template to render

def new_list(request):
    Item.objects.create(text=request.POST['item_text'])         # .objects.create is short for creating and saving new Item     = ... get the POST parameter (new to-do item)
    return redirect('/lists/the-only-list-in-the-world/')
