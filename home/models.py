from django.db import models
from django.core.validators import RegexValidator

class ContactMessage(models.Model):
    SERVICE_CHOICES = [
        ('web_design', 'Web Designing & Development'),
        ('graphic_design', 'Graphic Designing (Logo, Banner, Posters)'),
        ('seo', 'SEO Optimization & Digital Marketing'),
        ('social_media', 'Social Media Management'),
        ('branding', 'Branding & Business Identity'),
    ]

    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    country_name = models.CharField(max_length=100, default='')
    
    mobile_number = models.CharField(
        max_length=10,
        default='', 
        validators=[RegexValidator(regex=r'^\d{10}$', message='⚠️ Mobile number must be a Valid number⚠️')])

    services = models.JSONField(default=list)  # Multiple values store करने के लिए

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email} - {self.country_name} {self.mobile_number} - Services: {', '.join(self.services)}"

class CareerApplication(models.Model):
    JOB_ROLE_CHOICES = [
        ("commission_sales", "Commission based Sales Role"),
    ]

    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    job_role = models.CharField(max_length=50, choices=JOB_ROLE_CHOICES, default="commission_sales")
    
    def __str__(self):
        return self.name
