from django.test import TestCase
from django.urls import reverse, resolve
from home.views import index


class HomeViewTest(TestCase):
    def test_index_view(self):
        """Test if the index view returns a 200 status code and uses the correct template"""
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')


class HomeURLTest(TestCase):
    def test_home_url_resolves_to_index_view(self):
        """Test if the home URL ('/') resolves to the correct view"""
        resolver = resolve(reverse('home'))
        self.assertEqual(resolver.func, index)