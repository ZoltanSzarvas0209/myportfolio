from django.test import TestCase
from profiles.forms import UserProfileForm
from profiles.models import UserProfile


class UserProfileFormTests(TestCase):

    def test_user_profile_form_valid_data(self):
        """
        Test UserProfileForm with valid data
        """
        form = UserProfileForm(data={
            'default_phone_number': '1234567890',
            'default_country': 'Test Country',
            'default_postcode': '12345',
            'default_town_or_city': 'Test City',
            'default_street_address1': '123 Test St',
            'default_street_address2': 'Apt 1',
            'default_county': 'Test County',
        })
        self.assertTrue(form.is_valid())

    def test_user_profile_form_missing_required_field(self):
        """
        Test UserProfileForm with a missing required field (default_country)
        """
        form = UserProfileForm(data={
            'default_phone_number': '1234567890',
            'default_postcode': '12345',
            'default_town_or_city': 'Test City',
            'default_street_address1': '123 Test St',
            'default_street_address2': 'Apt 1',
            'default_county': 'Test County',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('default_country', form.errors)

    def test_user_profile_form_placeholders(self):
        """
        Test if the form fields have correct placeholders
        """
        form = UserProfileForm()
        self.assertEqual(form.fields['default_phone_number'].widget.attrs['placeholder'], 'Phone Number')
        self.assertEqual(form.fields['default_country'].widget.attrs['placeholder'], 'Country')
        self.assertEqual(form.fields['default_postcode'].widget.attrs['placeholder'], 'Postal Code')
        self.assertEqual(form.fields['default_town_or_city'].widget.attrs['placeholder'], 'Town or City')
        self.assertEqual(form.fields['default_street_address1'].widget.attrs['placeholder'], 'Street Address 1')
        self.assertEqual(form.fields['default_street_address2'].widget.attrs['placeholder'], 'Street Address 2')
        self.assertEqual(form.fields['default_county'].widget.attrs['placeholder'], 'County')
