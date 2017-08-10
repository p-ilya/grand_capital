from django.shortcuts import render, get_object_or_404
from .models import MenuNode

# Create your views here.


def index(request):
    page = get_object_or_404(MenuNode, slug='glavnaya')
    return render(request, 'menu/index.html', {'page': page})


def some_page(request, slug):
    page = get_object_or_404(MenuNode, slug=slug)
    return render(request, 'menu/some_page.html', {'page': page})
