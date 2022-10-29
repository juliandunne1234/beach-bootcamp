from django import forms
from django.contrib.auth.models import User
from .models import BootcampNextDate13, BookBootcamp13


class BookBootcampForm(forms.ModelForm):
    
    class Meta:
        model = BookBootcamp13
        fields = ('email', 'bootcamp_date')


class UpdateBookingForm(forms.ModelForm):
    
    class Meta:
        model = BookBootcamp13
        fields = ('email',)
