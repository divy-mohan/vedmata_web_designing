from django.shortcuts import render

# graphic Page View
def graphic_design(request):
    return render(request, 'services/graphic_design.html')

#web Page View
def web_design(request):
    return render(request, 'services/web_design.html')

#web Page View
def seo_services(request):
    return render(request, 'services/seo_services.html')
