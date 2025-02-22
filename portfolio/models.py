from django.db import models

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=254)
    description = models.TextField()
    image = models.ImageField(upload_to="project_images/", null=True, blank=True)
    deployed_url = models.URLField(max_length=500, null=True, blank=True)  # field for readme.md file for a project

    def __str__(self):
        return self.name