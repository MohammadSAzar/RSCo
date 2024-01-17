from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.db import transaction

from .models import CustomUser, UserType, DesignedUser, Profile


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields


class CaseCustomerSignUpForm(CustomUserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = UserType

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_case_customer = True
        user.save()
        # customer = DesignedUser.objects.create(user=user)
        return user


class ServiceCustomerSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = UserType

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_service_customer = True
        if commit:
            user.save()
        return user


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'sex', 'birthday', 'national_code', 'national_card', 'bank_card', 'auth_picture', 'country',
                  'province', 'city', 'postal_code', 'address', 'mobile_phone', 'pre_home_phone', 'home_phone']
