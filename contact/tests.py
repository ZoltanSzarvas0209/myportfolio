from django.test import TestCase
from .models import Contact
from django.urls import reverse, resolve
from .views import contact


class ContactModelTest(TestCase):
    def setUp(self):
        """
        Create a Contact instance for testing.
        """
        self.contact = Contact.objects.create(
            title="Test Message",
            content="This is a test message."
        )

    def test_contact_creation(self):
        """
        Test that the Contact object is created correctly.
        """
        self.assertEqual(self.contact.title, "Test Message")
        self.assertEqual(self.contact.content, "This is a test message.")
        self.assertIsNotNone(self.contact.updated_on)

    def test_contact_str_representation(self):
        """
        Test that the Contact model's __str__ method returns the title.
        """
        self.assertEqual(str(self.contact), "Test Message")


class ContactViewTest(TestCase):
    def test_contact_view_renders_correct_template(self):
        """
        Test that the contact view renders the correct template.
        """
        response = self.client.get(reverse("contact"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "contact/contact.html")


class TestUrls(TestCase):
    def test_contact_url_resolves(self):
        """
        Test that the contact URL correctly resolves to the contact view.
        """
        url = reverse("contact")
        self.assertEqual(resolve(url).func, contact)
