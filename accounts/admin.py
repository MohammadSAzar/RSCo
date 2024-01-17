from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser, Profile
from .forms import CustomUserCreationForm, CustomUserChangeForm


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Profile)



