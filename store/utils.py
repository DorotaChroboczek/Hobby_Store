import json
from .models import *


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


