from django.db import models
from django.contrib.auth.models import User


class Bootcamp(models.Model):
    """
    Bootcamp model
    """
    bootcamp_date = models.DateField()
    max_capacity = models.IntegerField(default=12)

    def __str__(self):
        return f"{self.bootcamp_date}"


class SignUp(models.Model):
    """
    SignUp model
    """
    full_name = models.CharField(max_length=80)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="signed_up")
    bootcamp = models.ForeignKey(Bootcamp, on_delete=models.CASCADE, related_name="bootcamps")
    email = models.EmailField(unique=True, default='')
    signup_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.full_name
