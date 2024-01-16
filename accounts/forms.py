from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.db import transaction

from .models import CustomUser, UserType, DesignedUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields


class CustomerSignUpForm(CustomUserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = UserType

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_student = True
        user.save()
        # customer = DesignedUser.objects.create(user=user)
        return user


class AgentSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = UserType

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_agent = True
        if commit:
            user.save()
        return user


