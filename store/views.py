import datetime

from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.generic import ListView, TemplateView

from .models import *

from .utils import *


class ContextListView(ListView):
    model = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = cart_data(request=self.request)

        cart_items = data['cart_items']
        order = data['order']
        items = data['items']

        context.update({
            'cart_items': cart_items,
            'items': items,
            'order': order,
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


class ContextTemplateView(TemplateView):
    model = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = cart_data(request=self.request)

        cart_items = data['cart_items']
        order = data['order']
        items = data['items']

        context.update({
            'cart_items': cart_items,
            'items': items,
            'order': order,
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


class HomeView(ContextListView):
    template_name = 'home.html'
    context_object_name = 'meta_products'
    model = MetaProduct

    def get_queryset(self):
        return MetaProduct.objects.all().order_by('name')


class CategoryView(ListView):
    template_name = 'category.html'
    model = Category

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = get_object_or_404(Category, id=self.kwargs['id'])
        subcategories = Subcategory.objects.filter(category=self.kwargs['id']).order_by('name').all()
        context = {
            'category': category,
            'subcategories': subcategories,
            'overcategories': Overcategory.objects.all(),
            'c_modelings': Category.objects.filter(overcategory__name='Modeling').order_by('name').all(),
            'c_sculptures': Category.objects.filter(overcategory__name='Sculpture').order_by('name').all(),
            'c_paintings': Category.objects.filter(overcategory__name='Painting').order_by('name').all(),
            'c_photos': Category.objects.filter(overcategory__name='Photography').order_by('name').all(),
            'c_writings': Category.objects.filter(overcategory__name='Writing').order_by('name').all(),
            'c_landscapes': Category.objects.filter(overcategory__name='Landscape Modeling').order_by('name').all(),
            'c_giftsets': Category.objects.filter(overcategory__name='Gift Sets').order_by('name').all(),
            'c_sales': Category.objects.filter(overcategory__name='Sales').order_by('name').all()
        }
        return context


class SubcategoryView(ListView):
    template_name = 'subcategory.html'
    model = Subcategory

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = get_object_or_404(Category, id=self.kwargs['c_id'])
        subcategory = get_object_or_404(Subcategory, id=self.kwargs['sc_id'])
        meta_products = MetaProduct.objects.filter(subcategory=self.kwargs['sc_id']).order_by('name').all()
        context = {
            'category': category,
            'subcategory': subcategory,
            'meta_products': meta_products,
            'overcategories': Overcategory.objects.all(),
            'c_modelings': Category.objects.filter(overcategory__name='Modeling').order_by('name').all(),
            'c_sculptures': Category.objects.filter(overcategory__name='Sculpture').order_by('name').all(),
            'c_paintings': Category.objects.filter(overcategory__name='Painting').order_by('name').all(),
            'c_photos': Category.objects.filter(overcategory__name='Photography').order_by('name').all(),
            'c_writings': Category.objects.filter(overcategory__name='Writing').order_by('name').all(),
            'c_landscapes': Category.objects.filter(overcategory__name='Landscape Modeling').order_by('name').all(),
            'c_giftsets': Category.objects.filter(overcategory__name='Gift Sets').order_by('name').all(),
            'c_sales': Category.objects.filter(overcategory__name='Sales').order_by('name').all()
        }
        return context


class MetaProductView(ListView):
    template_name = 'meta_product.html'
    model = MetaProduct

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = get_object_or_404(Category, id=self.kwargs['c_id'])
        subcategory = get_object_or_404(Subcategory, id=self.kwargs['sc_id'])
        meta_product = get_object_or_404(MetaProduct, id=self.kwargs['mp_id'])
        products = Product.objects.filter(meta_product=meta_product).all()
        context = {
            'category': category,
            'subcategory': subcategory,
            'meta_product': meta_product,
            'products': products,
            'overcategories': Overcategory.objects.all(),
            'c_modelings': Category.objects.filter(overcategory__name='Modeling').order_by('name').all(),
            'c_sculptures': Category.objects.filter(overcategory__name='Sculpture').order_by('name').all(),
            'c_paintings': Category.objects.filter(overcategory__name='Painting').order_by('name').all(),
            'c_photos': Category.objects.filter(overcategory__name='Photography').order_by('name').all(),
            'c_writings': Category.objects.filter(overcategory__name='Writing').order_by('name').all(),
            'c_landscapes': Category.objects.filter(overcategory__name='Landscape Modeling').order_by('name').all(),
            'c_giftsets': Category.objects.filter(overcategory__name='Gift Sets').order_by('name').all(),
            'c_sales': Category.objects.filter(overcategory__name='Sales').order_by('name').all()
        }
        return context


class StoreMetaProductView(ListView):
    template_name = 'store_meta_product.html'
    model = MetaProduct

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        meta_product = get_object_or_404(MetaProduct, id=self.kwargs['id'])
        products = Product.objects.filter(meta_product=meta_product).all()
        category = meta_product.category
        context = {
            'meta_product': meta_product,
            'products': products,
            'category': category,
            'overcategories': Overcategory.objects.all(),
            'c_modelings': Category.objects.filter(overcategory__name='Modeling').order_by('name').all(),
            'c_sculptures': Category.objects.filter(overcategory__name='Sculpture').order_by('name').all(),
            'c_paintings': Category.objects.filter(overcategory__name='Painting').order_by('name').all(),
            'c_photos': Category.objects.filter(overcategory__name='Photography').order_by('name').all(),
            'c_writings': Category.objects.filter(overcategory__name='Writing').order_by('name').all(),
            'c_landscapes': Category.objects.filter(overcategory__name='Landscape Modeling').order_by('name').all(),
            'c_giftsets': Category.objects.filter(overcategory__name='Gift Sets').order_by('name').all(),
            'c_sales': Category.objects.filter(overcategory__name='Sales').order_by('name').all()
        }
        return context


def cart(request):
    data = cart_data(request)

    cart_items = data['cart_items']
    order = data['order']
    items = data['items']

    context = {
        'cart_items': cart_items,
        'items': items,
        'order': order
    }
    return render(request, 'cart.html', context)


def checkout(request):
    data = cart_data(request)

    cart_items = data['cart_items']
    order = data['order']
    items = data['items']

    context = {
        'cart_items': cart_items,
        'items': items,
        'order': order
    }
    return render(request, 'checkout.html', context)


def update_item(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action', action)
    print('ProductId:', productId)

    customer = request.user.profile
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    order_item, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        if product.availability >= 1:
            product.availability -= 1
            order_item.quantity += 1
        else:
            return JsonResponse('Item is not availability', safe=False)

    elif action == 'remove':
        order_item.quantity -= 1
        product.availability += 1

    order_item.save()

    if order_item.quantity <= 0:
        order_item.delete()

    return JsonResponse('Item was added', safe=False)


def process_order(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.profile
        order, created = Order.objects.get_or_create(customer=customer, complete=False)

    else:
        customer, order = quest_order(request, data)

    total = float(data['form']['total'])
    order.transaction_id = transaction_id

    if total == order.get_cart_total:
        order.complete = True
    order.save()

    if order.shipping is True:
        ShippingAddress.objects.create(
            customer=customer,
            order=order,
            address=data['shipping']['address'],
            city=data['shipping']['city'],
            state=data['shipping']['state'],
            zipcode=data['shipping']['zipcode'],
        )

    return JsonResponse('Payment complete!', safe=False)
