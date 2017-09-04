from django import forms
from .models import expense
import re


class expenseForm(forms.ModelForm):

    class Meta:
        model = expense
        fields = ['category', 'price', 'Description']

    def clean_category(self):
        category = self.cleaned_data['category']
        if bool(re.match(r'.*\d', category)):
            raise forms.ValidationError("Enter Only Category")
        else:
            return category
