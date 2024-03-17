from django.urls import path
from . import views

# URL patterns for the Account app
urlpatterns = [
    path("", views.home, name="home_name"),
    path("register_needy/", views.register_needy, name="register_needy_name"),
    path("details/<int:id>/", views.details, name="details_name"),
    path("edit_needy/", views.edit_needy, name="edit_needy_name"),
]
