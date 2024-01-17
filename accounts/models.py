from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class Profile(models.Model):
    SEX_CHOICES = [
        ('m', _('Male')),
        ('f', _('Female')),
    ]
    APPROVAL_STATUS_CHOICES = [
        ('a', _('Approved')),
        ('r', _('Rejected')),
        ('w', _('Waiting')),
    ]
    avatar = models.ImageField(upload_to='profiles/avatars/', default='default.jpg')
    sex = models.CharField(max_length=10, choices=SEX_CHOICES, blank=True)
    birthday = models.DateField(auto_now_add=False, blank=True)
    national_code = models.CharField(max_length=10, blank=True)
    national_card = models.ImageField(upload_to='profiles/national_cards/', blank=True)
    bank_card = models.ImageField(upload_to='profiles/bank_cards/', blank=True)
    auth_picture = models.ImageField(upload_to='profiles/auths/', blank=True)
    country = models.CharField(max_length=150, blank=True)
    province = models.CharField(max_length=150, blank=True)
    city = models.CharField(max_length=150, blank=True)
    postal_code = models.CharField(max_length=10, blank=True)
    address = models.CharField(max_length=1000, blank=True)
    mobile_phone = models.CharField(max_length=11)
    home_phone = models.CharField(max_length=8, blank=True)
    pre_home_phone = models.CharField(max_length=3, blank=True)
    status = models.CharField(max_length=10, choices=APPROVAL_STATUS_CHOICES, blank=True)

    # def __str__(self):
    #     return f' کاربر:{self.user.first_name} {self.user.last_name}'

class CustomUser(AbstractUser):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name='user', null=True)


class UserType(CustomUser):
    is_case_customer = models.BooleanField(default=False)
    is_service_customer = models.BooleanField(default=False)

class DesignedUser(models.Model):
    user_type = models.OneToOneField(UserType, on_delete=models.CASCADE, primary_key=True)

