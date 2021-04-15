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
            'c_modelings': Category.objects.filter(overcategory__name='Modeling').order_by('name').all(),
            'c_sculptures': Category.objects.filter(overcategory__name='Sculpture').order_by('name').all(),
            'c_paintings': Category.objects.filter(overcategory__name='Painting').order_by('name').all(),
            'c_photos': Category.objects.filter(overcategory__name='Photography').order_by('name').all(),
            'c_writings': Category.objects.filter(overcategory__name='Writing').order_by('name').all(),
            'c_landscapes': Category.objects.filter(overcategory__name='Landscape Modeling').order_by('name').all(),
            'c_giftsets': Category.objects.filter(overcategory__name='Gift Sets').order_by('name').all(),
            'c_sales': Category.objects.filter(overcategory__name='Sales').order_by('name').all(),
        })
        return context

    def get_queryset(self):
        return MetaProduct.objects.all().order_by('name')


