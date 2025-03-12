from decimal import Decimal
from services.models import Service
from checkout.models import Order, OrderLineItem
from django.test import TestCase, Client
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from checkout.views import checkout, checkout_success


class OrderModelTest(TestCase):
    def setUp(self):
        self.order = Order.objects.create(
            full_name="John Doe",
            email="john@example.com",
            phone_number="1234567890",
            country="US",
            town_or_city="New York",
            street_address1="123 Main St",
        )

    def test_order_number_generated(self):
        """Test that an order number is generated on save"""
        self.assertIsNotNone(self.order.order_number)
        self.assertEqual(len(self.order.order_number), 32)

    def test_update_total(self):
        """Test update_total correctly calculates order total"""
        service = Service.objects.create(name="Test Service",
                                         price=Decimal("50.00"))
        _ = OrderLineItem.objects.create(order=self.order,
                                         service=service, quantity=2)
        self.order.update_total()
        self.assertEqual(self.order.order_total, Decimal("100.00"))


class OrderLineItemModelTest(TestCase):
    def setUp(self):
        self.order = Order.objects.create(
            full_name="John Doe",
            email="john@example.com",
            phone_number="1234567890",
            country="US",
            town_or_city="New York",
            street_address1="123 Main St",
        )
        self.service = Service.objects.create(name="Test Service",
                                              price=Decimal("25.00"))

    def test_lineitem_total_calculated(self):
        """Test that lineitem_total is correctly calculated on save"""
        line_item = OrderLineItem.objects.create(order=self.order,
                                                 service=self.service,
                                                 quantity=3)
        self.assertEqual(line_item.lineitem_total, Decimal("75.00"))

    def test_order_total_updates_on_lineitem_save(self):
        """Test that saving a line item updates the order total"""
        _ = OrderLineItem.objects.create(order=self.order,
                                         service=self.service,
                                         quantity=2)
        self.order.refresh_from_db()
        self.assertEqual(self.order.order_total, Decimal("50.00"))


class CheckoutViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser',
                                             password='testpass')
        self.client.login(username='testuser', password='testpass')
        self.checkout_url = reverse('checkout')
        self.success_url = reverse('checkout_success', args=['123ABC'])

        self.order = Order.objects.create(
            order_number='123ABC',
            full_name="John Doe",
            email="john@example.com",
            phone_number="1234567890",
            country="US",
            town_or_city="New York",
            street_address1="123 Main St",
        )

    def test_checkout_success_renders_correct_template(self):
        """Test checkout success page renders checkout_success.html template"""
        response = self.client.get(reverse('checkout_success',
                                           args=[self.order.order_number]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/checkout_success.html')


class CheckoutURLsTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_checkout_url_resolves(self):
        """Test checkout URL resolves to the correct view"""
        url = reverse('checkout')
        self.assertEqual(resolve(url).func, checkout)

    def test_checkout_success_url_resolves(self):
        """Test checkout success URL resolves to the correct view"""
        url = reverse('checkout_success', args=['123ABC'])
        self.assertEqual(resolve(url).func, checkout_success)
