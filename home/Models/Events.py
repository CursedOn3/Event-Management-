from django.db import models

from home.Models.Customer import Customer


class Event(models.Model):
    name = models.CharField(max_length=50)
    venue = models.CharField(max_length=50)
    ticket_price = models.FloatField()
    event_date = models.DateField()
    booked = models.BooleanField()


