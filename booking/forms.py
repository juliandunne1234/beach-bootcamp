# from .models import SignUp
# from django import forms


# class SignUpForm(forms.ModelForm):
    
#     class Meta:
#         model = SignUp
#         fields = ('full_name', 'bootcamp_date', 'email')

##########################################################################
from django import forms
from django.contrib.auth.models import User
from .models import BookingBootcamp


class UserForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ('username', 'email')


class BookingForm(forms.ModelForm):
    
    class Meta:
        model = BookingBootcamp
        fields = ('bootcamp_date',)
