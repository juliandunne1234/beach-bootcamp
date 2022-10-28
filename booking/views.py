# from django.shortcuts import render, reverse
# from django.views import View
# from django.http import HttpResponseRedirect
# from django.contrib import messages
# from .models import SignUp
# from .forms import SignUpForm


# def current_registrations(bootcamp_date):

#     current_registrations = len(SignUp.objects.filter(
#         bootcamp_date=bootcamp_date,)
#         )

#     return current_registrations


# def bootcamp_capacity(booking_confirmed):

#     max_capacity = 12
#     available_spaces = max_capacity - booking_confirmed

#     return available_spaces


# class BootcampRegistration(View):

#     def get(self, request, *args, **kwargs):

#         return render(
#             request,
#             "registration.html",
#             {
#                 "signup_form": SignUpForm(),
#             }
#         )
    
#     def post(self, request, *args, **kwargs):

#         bootcamp_registration_form = SignUpForm(data=request.POST)

#         if bootcamp_registration_form.is_valid():
#             full_name = request.POST.get('full_name')
#             bootcamp_date = request.POST.get('bootcamp_date')
#             email = request.POST.get('email')
#             queryset = SignUp.objects.filter(email=email, bootcamp_date=bootcamp_date)
#             booking_confirmed = current_registrations(bootcamp_date)
#             available_spaces = bootcamp_capacity(booking_confirmed)
                        
#             if  queryset:
#                 messages.add_message(
#                         request, 
#                         messages.WARNING,
#                         f"Hi {full_name}, you have already registered for the {bootcamp_date} bootcamp!"
#                         )

#             elif available_spaces <= 0:
#                 messages.add_message(
#                         request,
#                         messages.INFO,
#                         f"Hi {full_name}, sorry due to demand {bootcamp_date} bootcamp is fully booked! "
#                         f"Please select another bootcamp."
#                         )

#             else:
#                 bootcamp_registration_form.save()
#                 messages.add_message(
#                         request, 
#                         messages.SUCCESS,
#                         f"Hi {full_name}, thank you for registering for the {bootcamp_date} bootcamp!"
#                         )

#             return HttpResponseRedirect(
#                     reverse("index",)               
#                 )

#         else:
#             return render(
#             request,
#             "registration.html",
#             {
#                 "signup_form": SignUpForm()
#             }
#         )

###############################################################################

# from django.shortcuts import render, reverse
# from django.views import View
# from django.http import HttpResponseRedirect
# from .models import BookingBootcamp
# from .forms import BookingForm, UserForm


# class BootcampRegistration(View):

#     def get(self, request, *args, **kwargs):

#         return render(
#             request,
#             "registration.html",
#             {
#                 "booking_form": BookingForm(),
#                 "user_form": UserForm(),
#             }
#         )
    
#     def post(self, request, *args, **kwargs):

#         user_registration_form = UserForm(data=request.POST)
#         booking_registration_form = BookingForm(data=request.POST)

#         if user_registration_form.is_valid() and booking_registration_form.is_valid():
#             user_name = request.POST.get('username')
#             email = request.POST.get('email')
#             bootcamp_date = request.POST.get('bootcamp_date')
#             user = user_registration_form.save()
#             user_booking = booking_registration_form.save(commit=False)
#             user_booking.user = user
#             user_booking.save()

#             return HttpResponseRedirect(
#                     reverse("index",)               
#                 )

#         else:
#             return render(
#             request,
#             "registration.html",
#             {
#                 "booking_form": BookingForm(),
#                 "user_form": UserForm(),
#             }
#         )

###############################################################################

from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.views import View
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from .models import BootcampNextDate13, BookBootcamp13
from .forms import BookBootcampForm, UpdateBookingForm


class BootcampRegistration(View):

    def get(self, request, *args, **kwargs):

        return render(
            request,
            "registration.html",
            {
                "booking_details": BookBootcampForm(),
            }
        )  
    

    def post(self, request, *args, **kwargs):

        bootcamp_booking_details = BookBootcampForm(data=request.POST)
        
        if bootcamp_booking_details.is_valid():

            bootcamp_booking_details.instance.name = request.user.username
            bootcamp_booking_details.email = request.POST.get('email')
            bootcamp_booking_details.bootcamp_date = request.POST.get('bootcamp_date')
            bootcamp_booking_details.save()

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

        id = id
        user_registration = get_object_or_404(BookBootcamp13, pk=id)
        user_registration.delete()

        current_registration = BookBootcamp13.objects.all()

        return HttpResponseRedirect(reverse("index"))


class UpdateRegistration(View):

    def get(self, request, *args, **kwargs):

        current_registration = BookBootcamp13.objects.all()

        return render(
            request,
            "update_registration.html",
            {
                "current_registration": current_registration,
                "booking_details": BookBootcampForm(),
            }
        )


def update_registration(request, id):
    item = get_object_or_404(BookBootcamp13, pk=id)
    if request.method == 'POST':
        form = UpdateBookingForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(
                    reverse("index",)               
                )
    return HttpResponseRedirect(
                    reverse("index",)               
                )