# from .models import SignUp
# from django import forms


# class SignUpForm(forms.ModelForm):
    
#     class Meta:
#         model = SignUp
#         fields = ('full_name', 'bootcamp_date', 'email')

##########################################################################
# from django import forms
# from django.contrib.auth.models import User
# from .models import BookingBootcamp


# class UserForm(forms.ModelForm):
    
#     class Meta:
#         model = User
#         fields = ('username', 'email')


# class BookingForm(forms.ModelForm):
    
#     class Meta:
#         model = BookingBootcamp
#         fields = ('bootcamp_date',)


##########################################################################

# from django import forms
# from django.contrib.auth.models import User
# from .models import BookingBootcamp


# class UserForm(forms.ModelForm):
    
#     class Meta:
#         model = User
#         fields = ('username', 'email')


# class BookingForm(forms.ModelForm):
    
#     class Meta:
#         model = BookingBootcamp
#         fields = ('bootcamp_date',)

##########################################################################

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import BootcampDate


class CreateUserForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class BookingDateForm(forms.ModelForm):
    
    class Meta:
        model = BootcampDate
        fields = ('next_bootcamp',)
