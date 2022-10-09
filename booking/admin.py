from django.contrib import admin
from .models import SignUp


@admin.register(SignUp)
class SignUpAdmin(admin.ModelAdmin):
    """
    SignUpAdmin class
    """
    list_display = ('full_name', 'bootcamp_date', 'email', 'signup_date')
    list_filter = ('full_name', 'bootcamp_date', 'email', 'signup_date')
