from django.db import models


class Pizza(models.Model):
    """A pizza the user is learning about"""

    name = models.CharField(max_length=200)
    add_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model"""
        return self.name


class Topping(models.Model):
    """A topping the user is learning about"""

    name = models.CharField(max_length=200)
    add_date = models.DateTimeField(auto_now_add=True)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)

    def __str__(self):
        """Return a string representation of the model"""
        return self.name


# Create your models here.
