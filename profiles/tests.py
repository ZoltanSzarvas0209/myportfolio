from django.test import TestCase
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from profiles.models import UserProfile
from checkout.models import Order
from profiles.views import profile, order_history


class UserProfileModelTest(TestCase):

    def setUp(self):
        """
        Create a test user before each test
        """
        self.user = User.objects.create_user(username='testuser', password='testpass123')

    def test_user_profile_created_on_user_creation(self):
        """
        Test that a UserProfile is automatically created when a new User is created
        """
        profile = UserProfile.objects.get(user=self.user)
        self.assertIsInstance(profile, UserProfile)
        self.assertEqual(profile.user.username, 'testuser')

    def test_user_profile_str_method(self):
        """
        Test the __str__ method of the UserProfile model
        """
        profile = UserProfile.objects.get(user=self.user)
        self.assertEqual(str(profile), 'testuser')

    def test_update_user_profile(self):
        """
        Test updating user profile fields
        """
        profile = UserProfile.objects.get(user=self.user)
        profile.default_phone_number = "1234567890"
        profile.default_country = "USA"
        profile.default_postcode = "10001"
        profile.default_town_or_city = "New York"
        profile.default_street_address1 = "123 Main St"
        profile.default_street_address2 = "Apt 4B"
        profile.default_county = "New York County"
        profile.save()

        updated_profile = UserProfile.objects.get(user=self.user)
        self.assertEqual(updated_profile.default_phone_number, "1234567890")
        self.assertEqual(updated_profile.default_country, "USA")
        self.assertEqual(updated_profile.default_postcode, "10001")
        self.assertEqual(updated_profile.default_town_or_city, "New York")
        self.assertEqual(updated_profile.default_street_address1, "123 Main St")
        self.assertEqual(updated_profile.default_street_address2, "Apt 4B")
        self.assertEqual(updated_profile.default_county, "New York County")


class ProfileViewTemplateTests(TestCase):

    def setUp(self):
        """
        Set up a test user and profile before each test
        """
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        self.profile = UserProfile.objects.get(user=self.user)  # Auto-created by signal

    def test_profile_view_renders_correct_template(self):
        """
        Test that the profile view renders the correct template
        """
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')


class OrderHistoryViewTemplateTests(TestCase):

    def setUp(self):
        """
        Set up a test user, profile, and order before each test
        """
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        self.profile = UserProfile.objects.get(user=self.user)
        self.order = Order.objects.create(
            order_number="123456",
            user_profile=self.profile,
            full_name="Test User",
            email="test@example.com",
            phone_number="123456789",
            country="Test Country",
            postcode="12345",
            town_or_city="Test City",
            street_address1="123 Test St",
            street_address2="Apt 1",
            county="Test County",
            order_total=100.00,
        )

    def test_order_history_view_renders_correct_template(self):
        """
        Test that the order history view renders the correct template
        """
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('order_history', args=[self.order.order_number]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/checkout_success.html')


class TestProfilesUrls(TestCase):

    def test_profile_url_resolves(self):
        """
        Test if the profile URL resolves to the correct view
        """
        url = reverse('profile')
        self.assertEqual(resolve(url).func, profile)

    def test_order_history_url_resolves(self):
        """
        Test if the order_history URL resolves to the correct view
        """
        url = reverse('order_history', args=['123456'])
        self.assertEqual(resolve(url).func, order_history)