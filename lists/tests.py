from django.test import TestCase

class HomePageTest(TestCase):
    def test_uses_home_template(self):      # HTTP GET Request requests data from a specified resource
        response = self.client.get('/')     # calls the home_page view function indirectly (via url mapping), because the given URL is root (home)
        self.assertTemplateUsed(response, 'home.html')
    def test_can_save_a_POST_request(self):                                     # HTTP POST Request submits data to be processed to a specified resource
        response = self.client.post('/', data={'item_text': 'A new list item'}) # to do a POST, call self.client.post: 'data' argument contains the form data we want to send
        self.assertIn('A new list item', response.content.decode())
        self.assertTemplateUsed(response, 'home.html')
