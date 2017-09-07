from django import forms
from .models import ExpenseDetails


class ExpenseDetailsForm(forms.ModelForm):

    class Meta:
        model = ExpenseDetails
        fields = ['category', 'price', 'description', 'owner']
        widgets = {
            'owner': forms.HiddenInput(),
            'category': forms.TextInput(attrs={
                'placeholder': 'category',
                'class': 'form-control',
            }),
            'description': forms.TextInput(attrs={
                'placeholder': 'Description',
                'class': 'form-control',
            }),
            'price': forms.TextInput(attrs={
                'placeholder': 'price',
                'class': 'form-control',
            }),
        }
