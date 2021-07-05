from django.db import models
from django.forms import fields
from .models import Stock
from django import forms

class StockCreateForm(forms.ModelForm):
    class Meta:
        model=Stock
        fields=['category', 'item_name', 'quantity']