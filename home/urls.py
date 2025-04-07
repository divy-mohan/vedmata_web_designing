from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page URL pattern
    path('contact', views.contact_view, name='contact'),  # Contact page URL pattern
    path('careers', views.career_view, name='careers'),  # Careers page URL pattern
    path("thank_you/", views.thank_you_view, name="thank_you"),  # Thank you page URL pattern
    path('terms/', views.terms_view, name='terms'),  # Terms and Conditions page URL pattern
    path('refund/', views.refund_view, name='refund'),  # Refund Policy page URL pattern
    path('privacy/', views.privacy_view, name='privacy'),  # Privacy Policy page URL pattern
]
