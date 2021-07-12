from django.shortcuts import render, redirect
from .models import Product, Category

from django.views import View


# Create your views here.

class Homepage(View):
    def post(self, request):
        # add to card
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')  # session a card add hobe
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity == 1:  # remove  korte korte jodi 0 item hoi
                        # this item remove  from cart
                        cart.pop(product)
                    else:
                        cart[product] = quantity - 1
                else:
                    cart[product] = quantity + 1
            else:
                cart[product] = 1
        else:  # cart create
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        print("cart", cart)
        return redirect("AppShopStore:homepage")

    def get(self, request):
        # if session delete kore dei tahole empty session add korte hobe
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}

        # products = Product.get_all_products()
        products = None
        category = Category.get_all_category()

        categoryID = request.GET.get('category')  # url theke id ta recieved  korbe
        # first way
        # if categoryID:
        #     products = Product.objects.filter(category=categoryID)
        # else:
        #     products = Product.objects.all()
        # second way . first way is better
        if categoryID:
            products = Product.get_all_products_by_categoryId(categoryID)  # get_all_products_by_categoryId de a
            # categoryID pass hobe
        else:
            products = Product.get_all_products()
        print('your are : ', request.session.get('email'))

        # print(products)
        data = {
            "all_products": products,
            "all_category": category,
        }
        return render(request, 'App_shop/index.html', data)


class add_to_cart(View):
    def get(self, request):
        cart_ids = list(request.session.get('cart').keys())
        add_to_product = Product.objects.filter(id__in=cart_ids)
        data = {
            "add_to_product": add_to_product,
        }
        return render(request, 'App_shop/cart.html', data)
