from django.urls import path
from . import views
from adminpanel.views import login, register


urlpatterns = [
    # Profile Section
    path('login', login, name="login"),
    path('register', register, name="register")

   
]

