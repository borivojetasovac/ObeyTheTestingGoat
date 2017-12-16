from django.test import TestCase
from lists.models import Item, List

class HomePageTest(TestCase):
    def test_uses_home_template(self):      # HTTP GET Request requests data from a specified resource
        response = self.client.get('/')     # calls the home_page view function indirectly (via url mapping)
        self.assertTemplateUsed(response, 'home.html')

class NewListTest(TestCase):
    def test_can_save_a_POST_request(self):                                         # HTTP POST Request submits data to be processed to a specified resource
        self.client.post('/lists/new', data={'item_text': 'A new list item'})       # to do a POST, call self.client.post: 'data' argument contains the form data we want to send
        
        self.assertEqual(Item.objects.count(), 1)       # objects.count() is short for objects.all().count()
        new_item = Item.objects.first()                 # the same as objects.all()[0]
        self.assertEqual(new_item.text, 'A new list item')

    def test_redirects_after_POST(self):
        response = self.client.post('/lists/new', data={'item_text': 'A new list item'})    # to do a POST, call self.client.post: 'data' argument contains the form data we want to send
        new_list = List.objects.first()
        self.assertRedirects(response, f'/lists/{new_list.id}/')
    
class NewItemTest(TestCase):
    def test_can_save_a_POST_request_to_an_existing_list(self):
        other_list = List.objects.create()
        correct_list = List.objects.create()

        self.client.post(
                f'/lists/{correct_list.id}/add_item',
                data={'item_text': 'A new item for an existing list'}
        )

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new item for an existing list')
        self.assertEqual(new_item.list, correct_list)

    def test_redirects_to_list_view(self):
        other_list = List.objects.create()
        correct_list = List.objects.create()

        response = self.client.post(
                f'/lists/{correct_list.id}/add_item',
                data={'item_text': 'A new item for an existing list'}
        )

        self.assertRedirects(response, f'/lists/{correct_list.id}/')

class ListViewTest(TestCase):
    def test_uses_list_template(self):
        list_ = List.objects.create()
        response = self.client.get(f'/lists/{list_.id}/')
        self.assertTemplateUsed(response, 'list.html')

    def test_displays_only_items_for_that_list(self):
        correct_list = List.objects.create()
        Item.objects.create(text='itemey 1', list=correct_list)
        Item.objects.create(text='itemey 2', list=correct_list)
        other_list = List.objects.create()
        Item.objects.create(text='other list item 1', list=other_list)
        Item.objects.create(text='other list item 2', list=other_list)

        response = self.client.get(f'/lists/{correct_list.id}/')

        self.assertContains(response, 'itemey 1')       # knows how to deal with responses (no need for resopnse.content.decode())
        self.assertContains(response, 'itemey 2')
        self.assertNotContains(response, 'other list item 1')
        self.assertNotContains(response, 'other list item 2')

    def test_passes_correct_list_to_template(self):
        other_list = List.objects.create()
        correct_list = List.objects.create()
        response = self.client.get(f'/lists/{correct_list.id}/')
        self.assertEqual(response.context['list'], correct_list)