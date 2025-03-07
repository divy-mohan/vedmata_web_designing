from django.contrib import admin
from import_export.admin import ExportMixin
from import_export.resources import ModelResource
from .models import ContactMessage, CareerApplication

# Excel Export के लिए Resource Class
class ContactMessageResource(ModelResource):
    class Meta:
        model = ContactMessage

# ContactMessage के लिए Admin Configuration
@admin.register(ContactMessage)
class ContactMessageAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = ContactMessageResource
    list_display = ("name", "email", "created_at")
    search_fields = ("name", "email")
    list_filter = ("created_at",)

# CareerApplication के लिए Admin Configuration
@admin.register(CareerApplication)
class CareerApplicationAdmin(admin.ModelAdmin):
    list_display = ("name", "phone_number", "email", "job_role")
    search_fields = ("name", "email", "phone_number")
    list_filter = ("job_role",)
