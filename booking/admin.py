from django.contrib import admin
from .models import BootcampNextDate13, BookBootcamp13


@admin.register(BootcampNextDate13)
class BootcampNextDateAdmin(admin.ModelAdmin):

    list_display = ('next_bootcamp',)


@admin.register(BookBootcamp13)
class BookBootcampAdmin(admin.ModelAdmin):

    list_display = ('name', 'email', 'bootcamp_date')
