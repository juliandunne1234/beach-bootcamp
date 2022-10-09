from django.shortcuts import render, reverse
from django.views import View
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import SignUp
from .forms import SignUpForm


class BootcampRegistration(View):

    def get(self, request, *args, **kwargs):

        return render(
            request,
            "registration.html",
            {
                "signup_form": SignUpForm()
            }
        )
    
    def post(self, request, *args, **kwargs):

        bootcamp_registration_form = SignUpForm(data=request.POST)

        if bootcamp_registration_form.is_valid():
            full_name = request.POST.get('full_name')
            bootcamp_date = request.POST.get('bootcamp_date')
            email = request.POST.get('email')
            queryset = SignUp.objects.filter(email=email, bootcamp_date=bootcamp_date)

            if  queryset:
                messages.add_message(
                        request, messages.WARNING,
                        f"Hi {full_name}, you have already registered for the {bootcamp_date} bootcamp!")

            else:
                bootcamp_registration_form.save()
                messages.add_message(
                        request, messages.SUCCESS,
                        f"Hi {full_name}, thank you for registering for the {bootcamp_date} bootcamp!")

            return HttpResponseRedirect(
                    reverse("index",)               
                )
