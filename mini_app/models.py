from django.db import models

# Create your models here.

class User(models.Model):
    user_id = models.CharField(max_length=40)
    username = models.CharField(max_length=40)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)