from . import views
from django.urls import path


urlpatterns = [
    path('', views.BootcampRegistration.as_view(), name='registration_form'),
]
