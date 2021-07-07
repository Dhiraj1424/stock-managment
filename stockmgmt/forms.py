from django.db import models
from django.forms import fields
from .models import Stock
from django import forms

class StockCreateForm(forms.ModelForm):
    class Meta:
        model=Stock
        fields=['category', 'item_name', 'quantity']
        # custom validation form
    def clean_category(self):
        category=self.cleaned_data.get('category')
        if not category:
            raise forms.ValidationError(' dhiraj This field is required')
        for op in Stock.objects.all():
                if op.category==category:
                    raise forms.ValidationError(str(category) + ' is already created')
        return category

    def clean_item_name(self):
        item_name = self.cleaned_data.get('item_name')
        if not item_name:
	        raise forms.ValidationError('this is This field is required')
        return item_name


  
        

class StockSearchForm(forms.ModelForm):
    class Meta:
        model=Stock
        fields=['category','item_name']