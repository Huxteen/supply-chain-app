from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.

TITLE_CHOICES = (
    ("unknown", "unknown"),
    ("mr", "Mr"),
    ("mr", "Mrs"),
    ("dr", "Dr"),
    ("prof", "Prof"),
)


class Address(models.Model):
    """Address table"""
    company_name = models.CharField(max_length=255)
    contact_name = models.CharField(max_length=255)
    contact_title = models.CharField(
        max_length=20,
        choices=TITLE_CHOICES,
        default='unknown'
    )
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255, null=True, blank=True)
    postal_code = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255)
    fax = models.CharField(max_length=255, null=True, blank=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE,
                                related_name='address_user_id')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.company_name
