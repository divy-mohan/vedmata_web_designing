from django.contrib import admin
from import_export.admin import ExportMixin
from import_export.resources import ModelResource
from .models import ContactMessage

# Excel Export के लिए Resource Class बनाओ
class ContactMessageResource(ModelResource):
    class Meta:
        model = ContactMessage

# ExportMixin को शामिल करो
class ContactMessageAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = ContactMessageResource
    list_display = ('name', 'email', 'created_at')
    search_fields = ('name', 'email')
    list_filter = ('created_at',)

admin.site.register(ContactMessage, ContactMessageAdmin)
# Compare this snippet from vedmata_web_designing/home/views.py: