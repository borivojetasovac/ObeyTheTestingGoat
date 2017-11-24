from lists.models import Item
from django.test import TestCase

class HomePageTest(TestCase):
    def test_uses_home_template(self):      # HTTP GET Request requests data from a specified resource
        response = self.client.get('/')     # calls the home_page view function indirectly (via url mapping), because the given URL is root (home)
        self.assertTemplateUsed(response, 'home.html')
    def test_can_save_a_POST_request(self):                                     # HTTP POST Request submits data to be processed to a specified resource
        response = self.client.post('/', data={'item_text': 'A new list item'}) # to do a POST, call self.client.post: 'data' argument contains the form data we want to send
        
        self.assertEqual(Item.objects.count(), 1)       # objects.count() is short for objects.all().count()
        new_item = Item.objects.first()                 # the same as objects.all()[0]
        self.assertEqual(new_item.text, 'A new list item')
        
        self.assertIn('A new list item', response.content.decode())
        self.assertTemplateUsed(response, 'home.html')
    def test_only_saves_items_when_necessary(self):
        self.client.get('/')
        self.assertEqual(Item.objects.count(), 0)

class ItemModelTest(TestCase):
    def test_saving_and_retrieving_items(self):
        first_item = Item()
        first_item.text = 'The first (ever) list item'
        first_item.save()

        second_item = Item()
        second_item.text = 'Item the second'
        second_item.save()
        
        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'The first (ever) list item')
        self.assertEqual(second_saved_item.text, 'Item the second')
