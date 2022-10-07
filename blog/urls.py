from . import views
from django.urls import path


urlpatterns = [
    path('', views.PostList.as_view(), name='bootcamp_blog'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='bootcamp_post'),
]
