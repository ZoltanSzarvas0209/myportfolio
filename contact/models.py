from django.db import models

# Create your models here.

class Contact(models.Model):
    """
    A simple model designed
    to hold information about user
    messages.
    """
    title = models.CharField(max_length=200)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()

    def __str__(self):
        return self.title