from django.test import TestCase
from .models import Service
from django.core.exceptions import ValidationError
from decimal import Decimal
from django.urls import reverse, resolve
from .views import all_services, service_detail


class ServiceModelTest(TestCase):

    def setUp(self):
        """Set up a sample service instance for testing."""
        self.service = Service.objects.create(
            name="Web Development",
            description="Full-stack web development services.",
            price=Decimal("499.99"),
            image=None  # Testing without an image
        )

    def test_service_creation(self):
        """Test if the service instance is created successfully."""
        self.assertEqual(self.service.name, "Web Development")
        self.assertEqual(self.service.description, "Full-stack web development services.")
        self.assertEqual(self.service.price, Decimal("499.99"))

    def test_str_method(self):
        """Test the __str__ method of the model."""
        self.assertEqual(str(self.service), "Web Development")

    def test_price_max_digits(self):
        """Test if the price respects max_digits and decimal_places."""
        service = Service(
            name="Expensive Service",
            description="A costly service.",
            price=Decimal("12345678.99")
        )
        with self.assertRaises(ValidationError):
            service.full_clean()

    def test_price_negative_value(self):
        """Test that the price cannot be negative."""
        service = Service(
            name="Invalid Service",
            description="Should not allow negative pricing.",
            price=Decimal("-100.00")
        )
        with self.assertRaises(ValidationError):
            service.full_clean()


class ServiceViewsTest(TestCase):

    def setUp(self):
        """Set up test data for Service model."""
        self.service1 = Service.objects.create(
            name="Web Development",
            description="Full-stack web development services.",
            price=Decimal("499.99"),
        )
        self.service2 = Service.objects.create(
            name="SEO Optimization",
            description="Search engine optimization services.",
            price=Decimal("199.99"),
        )

    def test_all_services_view_renders_template(self):
        """Test if the all_services view renders the correct template."""
        response = self.client.get(reverse('services'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'services/services.html')

    def test_service_detail_view_renders_template(self):
        """Test if the service_detail view renders the correct template."""
        response = self.client.get(reverse('service_detail', args=[self.service1.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'services/service_detail.html')

    def test_service_detail_view_404_renders_default_template(self):
        """Test if requesting a non-existent service returns a 404 and uses the correct template (if customized)."""
        response = self.client.get(reverse('service_detail', args=[999]))
        self.assertEqual(response.status_code, 404)


class ServiceURLsTest(TestCase):

    def setUp(self):
        """Set up test data for URLs."""
        self.service = Service.objects.create(
            name="Web Development",
            description="Full-stack web development services.",
            price=Decimal("499.99"),
        )

    def test_all_services_url_resolves(self):
        """Test if the services URL resolves to the correct view."""
        url = reverse('services')
        self.assertEqual(resolve(url).func, all_services)

    def test_service_detail_url_resolves(self):
        """Test if the service_detail URL resolves to the correct view."""
        url = reverse('service_detail', args=[self.service.id])
        self.assertEqual(resolve(url).func, service_detail)
