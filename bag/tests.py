from django.test import TestCase, Client
from django.urls import reverse, resolve
from services.models import Service
from django.contrib.messages import get_messages
from bag import views


class BagViewsTest(TestCase):

    def setUp(self):
        """Set up test client and create a service object."""
        self.client = Client()
        self.service = Service.objects.create(
            name="Test Service",
            price=100
        )
        self.bag_url = reverse('bag')
        self.add_to_bag_url = reverse('add_to_bag', args=[self.service.id])
        self.adjust_bag_url = reverse('adjust_bag', args=[self.service.id])
        self.remove_from_bag_url = reverse('remove_from_bag',
                                           args=[self.service.id])

    def test_bag_view_renders_correct_template(self):
        """Check if 'bag' view renders 'bag/bag.html'."""
        response = self.client.get(self.bag_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bag/bag.html')

    def test_add_to_bag_view(self):
        """Test adding a service to the shopping bag."""
        response = self.client.post(self.add_to_bag_url, {
            'quantity': 1,
            'redirect_url': self.bag_url
        })

        self.assertRedirects(response, self.bag_url)
        self.assertIn(str(self.service.id), self.client.session['bag'])
        self.assertEqual(self.client.session['bag'][str(self.service.id)], 1)

        messages = [msg.message for msg in get_messages(response.wsgi_request)]
        self.assertIn(f'Added {self.service.name} to your bag', messages)

    def test_adjust_bag_view(self):
        """Test adjusting quantity of an item in the shopping bag."""
        session = self.client.session
        session['bag'] = {str(self.service.id): 2}
        session.save()

        response = self.client.post(self.adjust_bag_url, {'quantity': 3})
        self.assertRedirects(response, self.bag_url)
        self.assertEqual(self.client.session['bag'][str(self.service.id)], 3)

    def test_remove_from_bag_view(self):
        """Test removing an item from the bag."""
        session = self.client.session
        session['bag'] = {str(self.service.id): 2}
        session.save()

        response = self.client.post(self.remove_from_bag_url)
        self.assertJSONEqual(response.content, {'success': True})
        self.assertNotIn(str(self.service.id), self.client.session['bag'])

        messages = [msg.message for msg in get_messages(response.wsgi_request)]
        self.assertIn(f'Succesfully removed {self.service.name}!', messages)


class TestBagUrls(TestCase):

    def test_bag_url_resolves(self):
        """Test if bag URL resolves to the correct view."""
        url = reverse('bag')
        self.assertEqual(resolve(url).func, views.bag)

    def test_add_to_bag_url_resolves(self):
        """Test if add_to_bag URL resolves correctly."""
        url = reverse('add_to_bag', args=['1'])
        self.assertEqual(resolve(url).func, views.add_to_bag)

    def test_adjust_bag_url_resolves(self):
        """Test if adjust_bag URL resolves correctly."""
        url = reverse('adjust_bag', args=['1'])
        self.assertEqual(resolve(url).func, views.adjust_bag)

    def test_remove_from_bag_url_resolves(self):
        """Test if remove_from_bag URL resolves correctly."""
        url = reverse('remove_from_bag', args=['1'])
        self.assertEqual(resolve(url).func, views.remove_from_bag)
