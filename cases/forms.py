from django import forms
from .models import Order


class AddToCart(forms.Form):
    CHOICES = [(i, str(i)) for i in range(1, 100)]
    meter = forms.TypedChoiceField(choices=CHOICES, coerce=int)
    inplace = forms.BooleanField(required=False, widget=forms.HiddenInput)


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'phone', 'address', 'national_code', 'notes']
        widgets = {
            'address': forms.Textarea(attrs={'rows': 3, 'placeholder': 'آدرس خود را وارد کنید...'}),
            'notes': forms.Textarea(attrs={'rows': 5, 'placeholder': 'توضیحات خود را وارد کنید...'}),
        }
