from django import forms
from .models import Orders


class OrdersForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = '__all__'

    labels = {
        'picture': 'Picture',
        'oid': 'Order ID',
        'fname': 'First Name',
        'lname': 'Last Name.',
        'price': 'Price',
        'mail': 'Email ID',
        'addr': 'Address',
    }

    widgets ={
        'picture': forms.ClearableFileInput(attrs={'placeholder': 'eg. just picture'}),
        'oid': forms.NumberInput(attrs={'placeholder': 'eg. 101'}),
        'fname': forms.TextInput(attrs={'placeholder': 'eg. Prosenjeet'}),
        'lname': forms.TextInput(attrs={'placeholder': 'eg. Shil'}),
        'price': forms.NumberInput(attrs={'placeholder': 'eg. 10000'}),
        'mail': forms.EmailInput(attrs={'placeholder': 'eg. abc@xyz.com'}),
        'addr': forms.Textarea(attrs={'placeholder': 'eg. IN'}),
    }