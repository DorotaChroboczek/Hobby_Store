from django.shortcuts import render
from django.views.generic import ListView

from .models import *


def home(request):
    overcategories = Overcategory.objects.all()
    categories = Category.objects.all()
    context = {'overcategories': overcategories,
               'categories': categories}
    return render(request, 'home.html', context)



