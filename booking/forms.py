from .models import SignUp
from django import forms


class SignUpForm(forms.ModelForm):
    
    class Meta:
        model = SignUp
        fields = ('full_name', 'bootcamp_date', 'email')
