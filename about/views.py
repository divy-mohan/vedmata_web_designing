from django.shortcuts import render

# Home Page View
def about_us(request):
    return render(request, 'about/about_us.html')
