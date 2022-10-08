from django.contrib import admin
from .models import Bootcamp, SignUp


@admin.register(Bootcamp)
class BootcampAdmin(admin.ModelAdmin):
    """
    BootcampAdmin class
    """
    list_display = ('bootcamp_date', 'max_capacity')
    list_filter = ('bootcamp_date',)


@admin.register(SignUp)
class SignUpAdmin(admin.ModelAdmin):
    """
    SignUpAdmin class
    """
    list_display = ('full_name', 'user', 'bootcamp', 'email', 'signup_date')
    list_filter = ('full_name', 'user', 'bootcamp', 'email', 'signup_date')
