from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.


class Service(models.Model):

    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to="service_images/",
                              null=True, blank=True)

    def __str__(self):
        return self.name

    def clean(self):
        if self.price < 0:
            raise ValidationError({"price": "Price cannot be negative."})
