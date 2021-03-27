from django.shortcuts import render

from .models import *


def home(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'home.html', context)

