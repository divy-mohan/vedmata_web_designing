from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm

# Home Page View
def home(request):
    return render(request, 'home/home.html')

# Contact Page View
def contact_view(request):
    form = ContactForm(request.POST or None)  # Preload form with data if POST request
    
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent successfully!")
            return redirect("thank_you")  # Redirect to 'thank_you' page after successful submission
        else:
            messages.error(request, "There was an error with your submission. Please check the form and try again.")

    return render(request, "home/contact.html", {"form": form})  # Form retains data on error

# Thank You Page View
def thank_you_view(request):
    return render(request, "home/thank_you.html")

# Terms and Conditions Page View
def terms_view(request):
    return render(request, "home/terms.html")

# Refund Policy Page View
def refund_view(request):
    return render(request, "home/refund.html")

# Privacy Policy Page View
def privacy_view(request):
    return render(request, "home/privacy.html")

from .forms import CareerApplicationForm  # CareerApplicationForm import किया

def career_view(request):
    if request.method == "POST":
        form = CareerApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Your application has been submitted successfully!")
            return redirect("thank_you")  # Redirect करने के लिए, URL name 'career' होना चाहिए
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = CareerApplicationForm()

    return render(request, "home/career_form.html", {"form": form})
