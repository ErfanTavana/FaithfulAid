from django.urls import path
from . import views

# URL patterns for the Account app
urlpatterns = [
    # Path for the login view, mapped to the login_view function in views.py
    path("login/", views.login_view, name="login"),
]
