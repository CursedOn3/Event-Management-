from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length= 120)
    email = models.CharField(max_length= 120)
    message = models.TextField()



class UserProfile(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    user_img = models.ImageField(upload_to='static/user_images/')


