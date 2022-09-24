from django.db import models
from django.contrib.auth.models import User


class Bootcamp(models.Model):
    """
    Bootcamp model
    """
    bootcamp_title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    bootcamp_date = models.DateField()
    max_capacity = models.IntegerField(default=12)

    def __str__(self):
        return self.bootcamp_title


class SignUp(models.Model):
    """
    SignUp model
    """
    full_name = models.CharField(max_length=80)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="signed_up")
    bootcamp = models.ForeignKey(Bootcamp, on_delete=models.CASCADE, related_name="bootcamps")
    signup_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.full_name
