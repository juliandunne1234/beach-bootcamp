from . import views
from django.urls import path


urlpatterns = [
    path('', views.BootcampRegistration.as_view(), name='registration_form'),
    path('cancel_reg/', views.CancelRegistration.as_view(), name='cancel_registration'),
    path('cancel_reg/<id>', views.CancelRegistration.as_view(), name='delete_registration'),
    path('update_reg/', views.UpdateRegistration.as_view(), name='update_registration'),
    # path('update_reg/<id>', views.UpdateRegistration.as_view(), name='update_email'),
    path('update_reg/', views.update_registration, name='update_bootcamp_date'),
    path('update_registration2/<id>', views.update_registration_email, name='update_registration_email'),
]
