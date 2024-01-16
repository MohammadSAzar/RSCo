from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    pass


class UserType(CustomUser):
    is_customer = models.BooleanField(default=False)
    is_agent = models.BooleanField(default=False)

class DesignedUser(models.Model):
    user_type = models.OneToOneField(UserType, on_delete=models.CASCADE, primary_key=True)



