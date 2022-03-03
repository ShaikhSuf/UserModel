from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(blank=False, unique=True, max_length=255, verbose_name="email")
    mobile_no = PhoneNumberField(blank=False, unique=True,verbose_name="mobileno" )

    USERNAME_FIELD = "username"
    EMAIL_FIELD =   "email"