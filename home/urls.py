from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page URL pattern
    path('contact', views.contact_view, name='contact'),  # Home page URL pattern
    path('careers', views.career_view, name='careers'),  # Home page URL pattern
    path("thank_you/", views.thank_you_view, name="thank_you"),
    # other URL patterns for your app
]
