# from django.contrib import admin
# from .models import SignUp


# @admin.register(SignUp)
# class SignUpAdmin(admin.ModelAdmin):
#     """
#     SignUpAdmin class
#     """
#     list_display = ('full_name', 'bootcamp_date', 'email', 'signup_date')
#     list_filter = ('full_name', 'bootcamp_date', 'email', 'signup_date')

##################################################################################

# from django.contrib import admin
# from .models import BookingBootcamp

# @admin.register(Bootcamp_Date)
# class BootcampDateAdmin(admin.ModelAdmin):

#     list_display = ('bootcamp_date',)


# @admin.register(BookingBootcamp)
# class BookingAdmin(admin.ModelAdmin):

#     list_display = ('user', 'bootcamp_date')

##################################################################################

from django.contrib import admin
from .models import BootcampNextDate12, BookBootcamp12

@admin.register(BootcampNextDate12)
class BootcampNextDateAdmin(admin.ModelAdmin):

    list_display = ('next_bootcamp',)


@admin.register(BookBootcamp12)
class BookBootcampAdmin(admin.ModelAdmin):

    list_display = ('name', 'email', 'bootcamp_date')
