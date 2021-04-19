import json
from .models import *
from accounts.models import Profile


def cookie_cart(request):
    try:
        cart = json.loads(request.COOKIES['cart'])
    # delete except later
    except:
        cart = {}

    print('Cart:', cart)
    items = []
    order = {'cart_total': 0, 'cart_items': 0, 'shipping': False}
    cart_items = order['cart_items']

    for c in cart:
        try:
            cart_items += cart[c]['quantity']
            product = Product.objects.get(id=c)
            total = (product.price * cart[c]['quantity'])
            # if product.promotion_price:
            #     total = (product.promotion_price ( cart[c]['quantity']))
            # else:
            #     total = (product.price * cart[c]['quantity'])

            order['cart_total'] += total
            order['cart_items'] += cart[c]['quantity']

            # need to add if statement for promotion_price
            item = {
                'product': {
                    'id': product.id,
                    'name': product.name,
                    'price': product.price,
                    'imageURL': product.imageURL,
                },
                'quantity': cart[c]['quantity'],
                'total': total,
            }
            items.append(item)

            if product.digital is False:
                order['shipping'] = True
        # delete except later
        except:
            pass
    return {'cart_items': cart_items, 'order': order, 'items': items}


def cart_data(request):
    if request.user.is_authenticated:
        customer = request.user.profile
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cart_items = order.cart_items
    else:
        cookie_data = cookie_cart(request)
        customer = None
        cart_items = cookie_data['cart_items']
        order = cookie_data['order']
        items = cookie_data['items']
    return {'customer': customer, 'cart_items': cart_items,
            'order': order, 'items': items}


def quest_order(request, data):
    print('User is not logged in...')
    print('COOKIES:', request.COOKIES)
    name = data['form']['name']
    email = data['form']['email']
    cookie_data = cookie_cart(request)
    items = cookie_data['items']

    customer, created = Profile.objects.get_or_create(
        email=email,
    )
    customer.name = name
    customer.save()

    order = Order.objects.create(
        customer=customer,
        complete=False,
    )

    for item in items:
        product = Product.objects.get(id=item['product']['id'])
        order_item = OrderItem.objects.create(
            product=product,
            order=order,
            quantity=item['quantity']
        )
    return customer, order
