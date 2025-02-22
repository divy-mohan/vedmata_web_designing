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