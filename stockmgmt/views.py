from django.shortcuts import redirect, render
from .models import*
from .forms import *

# Create your views here.


def home(request):
    title = "this is home page"
    context = {
        'title': title,
    }
    return render(request, 'stockmgmt/home.html', context)
#  db ma vayeko data lai page ma dekhauna


def list_item(request):

    titile = "this is title"
    queryset = Stock.objects.all()

    context = {
        'queryset': queryset
    }

    return render(request, 'stockmgmt/list_items.html', context)


def add_item(request):
    form = StockCreateForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('list_item')

    context = {
        'form': form
    }
    return render(request, 'stockmgmt/add_item.html', context)
