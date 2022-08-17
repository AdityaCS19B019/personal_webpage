from django.db import models

# Create your models here.

class User_Details(models.Model) :
    first_name = models.CharField(max_length=50)
    email_address = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    Org = models.CharField(max_length=50)

