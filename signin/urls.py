from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_login, name='login'),
    path('home', views.home, name='home'),
    path('signout', views.signout, name='signout')
]
