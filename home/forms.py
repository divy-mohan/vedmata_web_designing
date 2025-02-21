from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    services = forms.MultipleChoiceField(
        choices=ContactMessage.SERVICE_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=True,
        label="Choose Services which You Want"
    )

    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message', 'country_name', 'mobile_number', 'services']
