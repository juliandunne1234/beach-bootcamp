from . import views
from django.urls import path


urlpatterns = [
    path('', views.BootcampRegistration.as_view(), name='registration_form'),
    path('cancel_reg/', views.CancelRegistration.as_view(), name='cancel_registration'),
    path('cancel_reg/<id>', views.CancelRegistration.as_view(), name='delete_registration'),
    path('update_reg_info/<id>', views.update_registration_email, name='update_registration_info'),
]
