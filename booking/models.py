from django.db import models
from django.contrib.auth.models import User
import datetime


class BootcampNextDate13(models.Model):
    """
    Bootcamp date model
    """
    next_bootcamp = models.DateField(null=True)

    def __str__(self):
        return f"{self.next_bootcamp}"


class BookBootcamp13(models.Model):
    """
    Registraion model for bootcamp participants
    """
    name = models.CharField(max_length=80)
    email = models.EmailField()
    bootcamp_date = models.ForeignKey(BootcampNextDate13, on_delete=models.CASCADE, related_name="bootcamp_date")

    class Meta:
        unique_together = ['name', 'bootcamp_date']

    def __str__(self):
        return f"{self.email}"

