from django.urls import path
from . import views

urlpatterns = [
    path('', views.services_overview, name='services_overview'),  # Main services page
    path('graphic_design/', views.graphic_design, name='graphic_design'),  # URL pattern
    path('web_design/', views.web_design, name='web_design'),  # URL pattern
    path('seo_services/', views.seo_services, name='seo_services'),  # URL pattern
    path('text_to_audio/', views.text_to_audio, name='text_to_audio'),  # URL pattern
    path('audio_editing/', views.audio_editing, name='audio_editing'),  # URL pattern
    path('video_editing/', views.video_editing, name='video_editing'),  # URL pattern
]
