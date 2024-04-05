from django.db import models

from home.Models.Customer import Customer


class Venue(models.Model):
    name = models.CharField(max_length=120)
    location = models.CharField(max_length=120)
    status = models.TextField  # status can be: open, maintenance, closed [ set rule to allow booking among the statuses]
    created_at = models.DateTimeField
    updated_at = models.DateTimeField


class BookVenue(models.Model):
    booked_by = models.ForeignKey(Customer, on_delete=models.CASCADE)
    booked_on = models.DateTimeField
    booked_for = models.DateTimeField
    status = models.CharField(max_length=20)  # status can be : booked, paid
    created_at = models.DateTimeField
    updated_at = models.DateTimeField
