from django.contrib import admin
from .models import Bootcamp, SignUp


@admin.register(Bootcamp)
class BootcampAdmin(admin.ModelAdmin):
    """
    BootcampAdmin class
    """
    prepopulated_fields = {'slug': ('bootcamp_title',)}
    list_display = ('bootcamp_title', 'slug', 'bootcamp_date', 'max_capacity')
    list_filter = ('bootcamp_title', 'bootcamp_date')


@admin.register(SignUp)
class SignUpAdmin(admin.ModelAdmin):
    """
    SignUpAdmin class
    """
    list_display = ('full_name', 'user', 'bootcamp', 'signup_date')
    list_filter = ('full_name', 'user', 'bootcamp', 'signup_date')
