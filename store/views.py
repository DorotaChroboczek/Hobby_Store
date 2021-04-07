from django.shortcuts import render
from django.http import JsonResponse

from .models import *


def home(request):
    overcategories = Overcategory.objects.all()
    categories = Category.objects.all()
    context = {'overcategories': overcategories,
               'categories': categories}
    return render(request, 'home.html', context)



