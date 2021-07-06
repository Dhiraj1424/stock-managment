from .import views
from django.urls import path

urlpatterns = [
    path('', views.home, name="home"),
    path('list_item', views.list_item, name="list_item"),
    path('add_item', views.add_item, name="add_item")

]