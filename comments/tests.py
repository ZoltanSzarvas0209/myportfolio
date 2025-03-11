from django.test import TestCase
from django.contrib.auth.models import User
from portfolio.models import Project
from comments.models import Comment
from django.urls import reverse, resolve
from portfolio.views import edit_comment, delete_comment


class CommentModelTest(TestCase):
    def setUp(self):
        """Set up test data for the Comment model."""
        self.user = User.objects.create_user(username="testuser", password="password123")
        self.project = Project.objects.create(name="Test Project", description="Test Description")
        self.comment = Comment.objects.create(
            project=self.project,
            user=self.user,
            content="This is a test comment."
        )

    def test_comment_creation(self):
        """Test if the comment is created successfully."""
        self.assertEqual(self.comment.project, self.project)
        self.assertEqual(self.comment.user, self.user)
        self.assertEqual(self.comment.content, "This is a test comment.")
    
    def test_comment_str_method(self):
        """Test the string representation of the comment."""
        expected_str = f"Comment by {self.user.username} on {self.project.name}"
        self.assertEqual(str(self.comment), expected_str)

    def test_comment_timestamps(self):
        """Test if the comment's `created_at` field is auto-generated."""
        self.assertIsNotNone(self.comment.created_at)


class TestCommentURLs(TestCase):
    def test_edit_comment_url_resolves(self):
        """Test if the edit_comment URL resolves to the correct view."""
        url = reverse('edit_comment', args=[1])  # Testing with comment_id=1
        self.assertEqual(resolve(url).func, edit_comment)

    def test_delete_comment_url_resolves(self):
        """Test if the delete_comment URL resolves to the correct view."""
        url = reverse('delete_comment', args=[1])  # Testing with comment_id=1
        self.assertEqual(resolve(url).func, delete_comment)
