from django.shortcuts import render, reverse
from django.views import View
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import SignUp
from .forms import SignUpForm


def current_registrations(bootcamp_date):

    current_registrations = len(SignUp.objects.filter(
        bootcamp_date=bootcamp_date,)
        )

    return current_registrations


def bootcamp_capacity(booking_confirmed):

    max_capacity = 12
    available_spaces = max_capacity - booking_confirmed

    return available_spaces


class BootcampRegistration(View):

    def get(self, request, *args, **kwargs):

        return render(
            request,
            "registration.html",
            {
                "signup_form": SignUpForm(),
            }
        )
    
    def post(self, request, *args, **kwargs):

        bootcamp_registration_form = SignUpForm(data=request.POST)

        if bootcamp_registration_form.is_valid():
            full_name = request.POST.get('full_name')
            bootcamp_date = request.POST.get('bootcamp_date')
            email = request.POST.get('email')
            queryset = SignUp.objects.filter(email=email, bootcamp_date=bootcamp_date)
            booking_confirmed = current_registrations(bootcamp_date)
            available_spaces = bootcamp_capacity(booking_confirmed)
                        
            if  queryset:
                messages.add_message(
                        request, 
                        messages.WARNING,
                        f"Hi {full_name}, you have already registered for the {bootcamp_date} bootcamp!"
                        )

            elif available_spaces <= 0:
                messages.add_message(
                        request,
                        messages.INFO,
                        f"Hi {full_name}, sorry due to demand {bootcamp_date} bootcamp is fully booked! "
                        f"Please select another bootcamp."
                        )

            else:
                bootcamp_registration_form.save()
                messages.add_message(
                        request, 
                        messages.SUCCESS,
                        f"Hi {full_name}, thank you for registering for the {bootcamp_date} bootcamp!"
                        )

            return HttpResponseRedirect(
                    reverse("index",)               
                )

        else:
            return render(
            request,
            "registration.html",
            {
                "signup_form": SignUpForm()
            }
        )
