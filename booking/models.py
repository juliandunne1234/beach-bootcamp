# from django.db import models

# bootcamp_choices = (
#     ("November", "November"),
#     ("December", "December"),
#     ("January", "January"),
#     ("February", "February"),
#     ("March", "March"),
#     ("April", "April"),
#     )


# class SignUp(models.Model):
#     """
#     SignUp model
#     """
#     full_name = models.CharField(max_length=80)
#     bootcamp_date = models.CharField(max_length=10, choices=bootcamp_choices, default='')
#     email = models.EmailField(default='')
#     signup_date = models.DateField(auto_now_add=True)

#     def __str__(self):
#         return self.full_name


###############################################################################################

from django.db import models
from django.contrib.auth.models import User
import datetime


class BootcampNextDate12(models.Model):

    next_bootcamp = models.DateField(null=True)

    def __str__(self):
        return f"{self.next_bootcamp}"


class BookBootcamp12(models.Model):
    
    name = models.CharField(max_length=80)
    email = models.EmailField()
    bootcamp_date = models.ForeignKey(BootcampNextDate12, on_delete=models.CASCADE, related_name="bootcamp_date")

    class Meta:
        unique_together = ['name', 'bootcamp_date']

    def __str__(self):
        return f"{self.email}"

