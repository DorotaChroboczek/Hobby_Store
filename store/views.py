from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import ListView

from .models import *


class HomeView(ListView):
    template_name = 'home.html'
    context_object_name = 'meta_products'
    model = MetaProduct

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'overcategories': Overcategory.objects.all(),
            'categories': Category.objects.all()
        })
        return context

    def get_queryset(self):
        return MetaProduct.objects.all().order_by('name')

