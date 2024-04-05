from django.db import models

from home.Models.Customer import Customer


class Feedback(models.Model):
    message = models.CharField(max_length=120)
    created_by = models.ForeignKey(Customer, on_delete=models.CASCADE)
    created_at = models.DateTimeField
    updated_at = models.DateTimeField


