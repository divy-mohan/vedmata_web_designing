from django.urls import path
from . import views

urlpatterns = [
    path('graphic_design/', views.graphic_design, name='graphic_design'),  # URL pattern
    path('web_design/', views.web_design, name='web_design'),  # URL pattern
    path('seo_services/', views.seo_services, name='seo_services'),  # URL pattern
]
