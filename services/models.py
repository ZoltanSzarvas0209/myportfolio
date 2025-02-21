from django.db import models

# Create your models here.

class Service(models.Model):

    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to="service_images/", null=True, blank=True)

    def __str__(self):
        return self.name
