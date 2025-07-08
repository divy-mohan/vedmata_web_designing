from django.shortcuts import render

# Services Overview Page
def services_overview(request):
    return render(request, 'services/services_overview.html')

# graphic Page View
def graphic_design(request):
    return render(request, 'services/graphic_design.html')

#web Page View
def web_design(request):
    return render(request, 'services/web_design.html')

#web Page View
def seo_services(request):
    return render(request, 'services/seo_services.html')

# Text to Audio Page View
def text_to_audio(request):
    return render(request, 'services/text_to_audio.html')

# Audio Editing Page View
def audio_editing(request):
    return render(request, 'services/audio_editing.html')

# Video Editing Page View
def video_editing(request):
    return render(request, 'services/video_editing.html')
