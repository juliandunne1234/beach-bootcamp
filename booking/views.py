from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.views import View
from django.http import HttpResponseRedirect
from django.contrib import messages
import datetime
from django.contrib.auth.models import User
from .models import BootcampNextDate13, BookBootcamp13
from .forms import BookBootcampForm, UpdateBookingForm


# Function to calculate the number of current registrations
def current_registrations(bootcamp_date):

    current_registrations = len(BookBootcamp13.objects.filter(
        bootcamp_date=bootcamp_date,)
        )

    return current_registrations


# Function to calculate the number of places remaining in a bootcamp
def bootcamp_capacity(booking_confirmed):

    max_capacity = 3
    available_spaces = max_capacity - booking_confirmed

    return available_spaces


class BootcampRegistration(View):
    """
    Registration form to enter the bootcamp participants booking details
    """
    def get(self, request, *args, **kwargs):

        return render(
            request,
            "registration.html",
            {
                "booking_details": BookBootcampForm(),
            }
        )

    def post(self, request, *args, **kwargs):
        """
        Returns registration form booking details
        """
        bootcamp_booking_details = BookBootcampForm(data=request.POST)

        if bootcamp_booking_details.is_valid():

            bootcamp_booking_details.instance.name = request.user.username
            bootcamp_booking_details.email = request.POST.get('email')
            bootcamp_booking_details.bootcamp_date = request.POST.get('bootcamp_date')
            queryset = BookBootcamp13.objects.filter(name=bootcamp_booking_details.instance.name, bootcamp_date=bootcamp_booking_details.bootcamp_date)

            booking_confirmed = current_registrations(bootcamp_booking_details.bootcamp_date)
            available_spaces = bootcamp_capacity(booking_confirmed)

            if  queryset:
                messages.add_message(
                        request,
                        messages.WARNING,
                        f"Hi, you have already registered for the this bootcamp!"
                        )

            elif available_spaces <= 0:
                messages.add_message(
                        request,
                        messages.WARNING,
                        f"Hi {bootcamp_booking_details.instance.name}, sorry but due to demand this bootcamp is fully booked! "
                        )

            else:
                bootcamp_booking_details.save()
                messages.add_message(
                        request,
                        messages.SUCCESS,
                        f"Hi, thank you for registering for the bootcamp!"
                        )

            return HttpResponseRedirect(
                    reverse("index",)
                )

        else:
            return render(
                request,
                "registration.html",
                {
                    "booking_details": BookBootcampForm()
                }
            )


class CancelRegistration(View):
    """
    Return bootcamps the user is currently registered to attend
    """
    def get(self, request, *args, **kwargs):

        current_registration = BookBootcamp13.objects.all()

        return render(
            request,
            "cancel_registration.html",
            {
                "current_registration": current_registration,
            }
        )

    def post(self, request, id, *args, **kwargs):
        """
        Delete registrations for selected bootcamps only
        """
        id = id
        user_registration = get_object_or_404(BookBootcamp13, pk=id)
        user_registration.delete()

        messages.add_message(
                    request,
                    messages.ERROR,
                    f"Hi, you have cancelled your registration for this bootcamp!"
                    )

        return HttpResponseRedirect(reverse("index"))


def update_registration_email(request, id):
    """
    Update uuser registration contact email
    """
    current_registration = get_object_or_404(BookBootcamp13, id=id)

    if request.method == 'POST':
        form = UpdateBookingForm(request.POST, instance=current_registration)
        if form.is_valid():
            form.save()

            messages.add_message(
                    request,
                    messages.INFO,
                    f"Thank you for keeping your email up to date!"
                    )

            return HttpResponseRedirect(
                    reverse("index",)
                )

    form = UpdateBookingForm(instance=current_registration)

    return render(
            request,
            "update_registration.html",
            {
                "current_registration": current_registration,
                "registration_details": UpdateBookingForm(),
            }
        )
