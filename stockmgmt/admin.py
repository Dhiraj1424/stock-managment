from django.contrib import admin
from .forms import StockCreateForm

# Register your models here.
from .models import Stock


class StockCreateAdmin(admin.ModelAdmin):
    list_display = ['category', 'item_name', 'quantity']

    list_filter = ['category', 'item_name', 'last_updated']
    search_fields = ['category', 'item_name']
    # forms.py ma j xa admin site ma add garni bela ma ni teai dekhauxa
    form = StockCreateForm


admin.site.register(Stock, StockCreateAdmin)
