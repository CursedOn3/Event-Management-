from django.db import models

from home.Models.Customer import Customer
from home.Models.VenueOwner import Owner


class ChatMessages(models.Model):
    customer_id = models.ForeignKey(Customer,on_delete=models.CASCADE)
    owner_id = models.ForeignKey(Owner,on_delete=models.CASCADE)
    message = models.TextField
    created_at = models.DateTimeField
    updated_at = models.DateTimeField


