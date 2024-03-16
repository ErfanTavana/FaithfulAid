from django.urls import path
from . import views

# URL patterns for the Account app
urlpatterns = [
    path("register_needy/", views.register_needy, name="register_needy_name"),

]
