from django.shortcuts import render
from .models import*

# Create your views here.


def home(request):
    title = "this is home page"
    form = "this is home page"
    context = {
        'title': title,
        'ok':form
    }
    return render(request, 'stockmgmt/home.html', context)

def list_item(request):
    
    titile="this is title"
    queryset = Stock.objects.all()
    
    context={
            'queryset':queryset
    }

    return render(request,'stockmgmt/list_items.html', context)
