from django.db import models


class Roles(models.Model):
    role_name = models.CharField(max_length=120)
    created_at = models.DateTimeField
    updated_at = models.DateTimeField


