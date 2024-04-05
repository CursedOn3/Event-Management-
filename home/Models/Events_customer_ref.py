from django.contrib.auth.models import User
from django.db import models

from home.Models import Event
from home.Models.Customer import Customer


class EventCustomerRef(models.Model):
    customer_id = models.ForeignKey(User, on_delete=models.CASCADE)
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)


