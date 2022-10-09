from django.db import models

bootcamp_choices = (
    ("November", "November"),
    ("December", "December"),
    ("January", "January"),
    ("February", "February"),
    ("March", "March"),
    ("April", "April"),
    )


class SignUp(models.Model):
    """
    SignUp model
    """
    full_name = models.CharField(max_length=80)
    bootcamp_date = models.CharField(max_length=10, choices=bootcamp_choices, default='')
    email = models.EmailField(default='')
    signup_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.full_name
