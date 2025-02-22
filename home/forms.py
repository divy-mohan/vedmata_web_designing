from django import forms
from .models import ContactMessage
from .widgets import CustomCheckboxSelectMultiple

class ContactForm(forms.ModelForm):
    services = forms.MultipleChoiceField(
        choices=ContactMessage.SERVICE_CHOICES,
        widget=CustomCheckboxSelectMultiple,
        required=True,
        label="Choose Services which You Want"
    )

    email = forms.EmailField(
        required=True,
        error_messages={
            'invalid': "Please enter a valid email address."
        }
    )

    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message', 'country_name', 'mobile_number', 'services']
