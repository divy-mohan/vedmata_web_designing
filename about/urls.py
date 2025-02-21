from django.urls import path
from . import views

urlpatterns = [
    path('', views.about_us, name='about_us'),  # Home page URL pattern
    # other URL patterns for your app
]
