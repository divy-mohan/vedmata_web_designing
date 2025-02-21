from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm
from .models import ContactMessage

# Home Page View
def home(request):
    return render(request, 'home/home.html')

# Contact Page View
def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save the valid form data to the database
            form.save()
            messages.success(request, "Your message has been sent successfully!")
            return redirect("thank_you")  # Redirect to 'thank_you' page after successful submission
        else:
            # Handle form errors
            messages.error(request, "There was an error with your submission. Please try again.")
    else:
        form = ContactForm()

    # Render the contact form template
    return render(request, "home/contact.html", {"form": form})

# Thank You Page View
def thank_you_view(request):
    return render(request, "home/thank_you.html")


