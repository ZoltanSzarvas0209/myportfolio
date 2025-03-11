from django.test import TestCase
from checkout.forms import OrderForm

class OrderFormTest(TestCase):
    def test_valid_form(self):
        """Test form is valid with correct data"""
        form_data = {
            'full_name': 'John Doe',
            'email': 'john@example.com',
            'phone_number': '1234567890',
            'street_address1': '123 Main St',
            'street_address2': 'Apt 4B',
            'town_or_city': 'New York',
            'postcode': '10001',
            'country': 'US',
            'county': 'New York County',
        }
        form = OrderForm(data=form_data)
        self.assertTrue(form.is_valid())
    
    def test_missing_required_field(self):
        """Test form is invalid when a required field is missing"""
        form_data = {
            'email': 'john@example.com',
            'phone_number': '1234567890',
            'street_address1': '123 Main St',
            'town_or_city': 'New York',
            'postcode': '10001',
            'country': 'US',
            'county': 'New York County',
        }  # Missing 'full_name'
        form = OrderForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('full_name', form.errors)
    
    def test_placeholder_and_css_classes(self):
        """Test form fields have correct placeholders and CSS classes"""
        form = OrderForm()
        self.assertEqual(form.fields['full_name'].widget.attrs['placeholder'], 'Full Name *')
        self.assertEqual(form.fields['email'].widget.attrs['placeholder'], 'Email Address *')
        self.assertIn('stripe-style-input', form.fields['full_name'].widget.attrs['class'])