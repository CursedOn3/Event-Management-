from django.db import models


class VenueOwner(models.Model):
    fullname = models.CharField(max_length=120)
    username = models.CharField(max_length=120)
    password = models.CharField(max_length=120)
    created_at = models.DateTimeField
    updated_at = models.DateTimeField

