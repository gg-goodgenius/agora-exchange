from django.shortcuts import render
from django.views.generic import ListView
from django.http import HttpResponse
from core.models import Product

class MainView(ListView):
    model = Product
