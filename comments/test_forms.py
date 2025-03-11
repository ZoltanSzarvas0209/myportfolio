from django.test import TestCase
from comments.forms import CommentForm


class TestCommentForm(TestCase):
    def test_comment_form_valid_data(self):
        """Test if the form is valid with correct data."""
        form = CommentForm(data={'content': 'This is a test comment.'})
        self.assertTrue(form.is_valid())

    def test_comment_form_empty_data(self):
        """Test if the form is invalid when no data is provided."""
        form = CommentForm(data={})
        self.assertFalse(form.is_valid())
        self.assertIn('content', form.errors)
