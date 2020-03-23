from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Item


class HomeView(ListView):
    model = Item
    template_name = 'home.html'
    context_object_name = 'items'


class ItemDetailView(DetailView):
    model = Item
    template_name = 'product.html'
    context_object_name = 'item'


def checkout_page(request):
    return render(request, "checkout-page.html")
