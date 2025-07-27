from django.db import models

# Create your models here.
# waitlist/models.py
from django.db import models

class WaitlistEntry(models.Model):
    ROLE_CHOICES = [
        ('agency', 'Agency'),
        ('buyer', 'Buyer'),
        ('renter', 'Renter'),
        ('legal_firm', 'Legal Firm'),
    ]
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.email} ({self.get_role_display()})"
