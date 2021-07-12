from django import template

register = template.Library()


@register.filter(name='is_product_in_cart')
def is_product_in_cart(product, cart):
    keys = cart.keys()
    for Id in keys:
        try:
            if int(Id) == product.id:
                return True
        except ValueError:
            pass

    return False


@register.filter(name='cart_product_quantity')
def cart_product_quantity(product, cart):
    keys = cart.keys()
    for Id in keys:
        try:
            if int(Id) == product.id:
                return cart.get(Id)
        except:
            pass
    return 0


@register.filter(name='price_total')
def price_total(product, cart):
    return product.price * cart_product_quantity(product, cart)


@register.filter(name='total_cart_price')
def total_cart_price(products,cart):
    sum = 0
    for p in products:
        sum += price_total(p, cart)
    return sum
