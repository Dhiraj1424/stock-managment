from django.shortcuts import redirect, render
from .models import*
from .forms import *
from django.http import HttpResponse
import csv

# Create your views here.


def home(request):
    title = "this is home page"
    context = {
        'title': title,
    }
    return render(request, 'stockmgmt/home.html', context)
#  db ma vayeko data lai page ma dekhauna


def list_item(request):
    header = "this is title"
    form = StockSearchForm(request.POST or None)
    queryset = Stock.objects.all()

    context = {
        'header':header,
        'queryset': queryset,
        'form':form
    }
    


    if request.method == 'POST':
        queryset = Stock.objects.filter(
        # category__icontains=form['category'].value(),
        item_name__icontains=form['item_name'].value()
        )

        if form['export_to_CSV'].value() == True:
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="List of stock.csv"'
            writer = csv.writer(response)
            writer.writerow(['CATEGORY', 'ITEM NAME', 'QUANTITY'])
            instance = queryset
            for stock in instance:
                writer.writerow([stock.category, stock.item_name, stock.quantity])
            return response

        context = {
        "form": form,
        "header": header,
        "queryset": queryset,
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

def update_item(request,pk):
    stock=Stock.objects.get(id=pk)
    form=UpdateForm(instance=stock)
    if request.method=='POST':
        form=UpdateForm(request.POST,instance=stock)
        if form.is_valid():
            form.save()
            return redirect('/list_item')
    context={
        'form':form
    }
    return render(request, 'stockmgmt/add_item.html', context)

def delete_item(request,pk):
    stock=Stock.objects.get(id=pk)
    if request.method=='POST':
        stock.delete()
        return redirect('/list_item')

    context={
        'stock':stock
    }

    return render(request, 'stockmgmt/delete_item.html', context)

    

    
