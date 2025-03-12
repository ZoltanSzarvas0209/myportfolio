from django.test import TestCase
from .forms import Contact_form


class ContactFormTest(TestCase):
    def test_contact_form_valid_data(self):
        """
        Test if the form is valid with correct data.
        """
        form = Contact_form(data={
            "title": "Test Inquiry",
            "content": "This is a test message."
        })
        self.assertTrue(form.is_valid())

    def test_contact_form_missing_title(self):
        """
        Test that the form is invalid when 'title' is missing.
        """
        form = Contact_form(data={
            "title": "",  # Missing title
            "content": "This is a test message."
        })
        self.assertFalse(form.is_valid())
        self.assertIn("title", form.errors)

    def test_contact_form_missing_content(self):
        """
        Test that the form is invalid when 'content' is missing.
        """
        form = Contact_form(data={
            "title": "Test Inquiry",
            "content": ""
        })
        self.assertFalse(form.is_valid())
        self.assertIn("content", form.errors)

    def test_contact_form_empty_data(self):
        """
        Test that the form is invalid when no data is provided.
        """
        form = Contact_form(data={})
        self.assertFalse(form.is_valid())
        self.assertIn("title", form.errors)
        self.assertIn("content", form.errors)
