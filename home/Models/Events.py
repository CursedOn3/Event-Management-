from datetime import timezone, datetime, timedelta

from django.db import models

from home.Models.Customer import Customer
from datetime import timedelta

class Event(models.Model):
    name = models.CharField(max_length=50)
    venue = models.CharField(max_length=50)
    artist = models.CharField(max_length=50, default="Taylor Swift")
    ticket_price = models.FloatField()
    event_date = models.DateField()
    event_time_start = models.TimeField(default=datetime.now().strftime("%H:%M:%S"))
    event_time_end = models.TimeField(default=datetime.now().strftime("%H:%M:%S"))
    description = models.TextField(default="NA")
    booked = models.BooleanField()


