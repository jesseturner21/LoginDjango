from django.db import models

# User Model
class User(models.Model):
   username = models.CharField(max_length=200)
   password = models.CharField(max_length=200)
   