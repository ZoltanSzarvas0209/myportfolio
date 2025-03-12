from django.test import TestCase
from portfolio.models import Project
from django.contrib.auth.models import User
from django.urls import reverse, resolve
from portfolio.views import portfolio, about, tech, projects


class ProjectModelTest(TestCase):
    def setUp(self):
        self.project = Project.objects.create(
            name="Test Project",
            description="This is a test project description.",
            deployed_url="https://example.com",
            repo_url="https://github.com/example/repo"
        )

    def test_project_creation(self):
        """Test that a project is created successfully"""
        project = Project.objects.get(name="Test Project")
        self.assertEqual(project.name, "Test Project")
        self.assertEqual(project.description,
                         "This is a test project description.")
        self.assertEqual(project.deployed_url, "https://example.com")
        self.assertEqual(project.repo_url, "https://github.com/example/repo")
        self.assertEqual(project.image.name, "")

    def test_str_method(self):
        """Test the string representation of the Project model"""
        self.assertEqual(str(self.project), "Test Project")

    def test_optional_fields(self):
        """Test that optional fields can be left blank"""
        project = Project.objects.create(
            name="No URLs Project",
            description="This project has no URLs."
        )
        self.assertEqual(project.name, "No URLs Project")
        self.assertEqual(project.description, "This project has no URLs.")
        self.assertIsNone(project.deployed_url)
        self.assertIsNone(project.repo_url)
        self.assertIsNone(project.image.name)


class PortfolioViewsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser',
                                             password='testpassword')
        self.project = Project.objects.create(
            name="Test Project",
            description="This is a test project description.",
            deployed_url="https://example.com",
            repo_url="https://github.com/example/repo"
        )

    def test_portfolio_view(self):
        response = self.client.get(reverse('portfolio'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'portfolio/portfolio.html')

    def test_about_view(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'portfolio/about.html')

    def test_tech_view(self):
        response = self.client.get(reverse('tech'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'portfolio/tech.html')

    def test_projects_view(self):
        response = self.client.get(reverse('projects'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'portfolio/projects.html')
        self.assertIn('projects', response.context)


class TestUrls(TestCase):

    def test_portfolio_url_resolves(self):
        url = reverse('portfolio')
        self.assertEqual(resolve(url).func, portfolio)

    def test_about_url_resolves(self):
        url = reverse('about')
        self.assertEqual(resolve(url).func, about)

    def test_tech_url_resolves(self):
        url = reverse('tech')
        self.assertEqual(resolve(url).func, tech)

    def test_projects_url_resolves(self):
        url = reverse('projects')
        self.assertEqual(resolve(url).func, projects)
