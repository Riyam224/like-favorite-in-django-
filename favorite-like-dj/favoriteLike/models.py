from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(_("name"), max_length=50)
    like  = models.ManyToManyField(User, blank=True)

    # TODO: Define fields here

    class Meta:
        """Meta definition for Product."""

        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        """Unicode representation of Product."""
        return self.name
