from django.shortcuts import render
from .models import Product, Category


# Create your views here.

def Homepage(request):
    # products = Product.get_all_products()
    products = None
    category = Category.get_all_category()

    categoryID = request.GET.get('category')  # url theke id ta recieved  korbe
    if categoryID:
        products = Product.get_all_products_by_categoryId(categoryID) # get_all_products_by_categoryId de a categoryID pass hobe
    else:
        products = Product.get_all_products()

    # print(products)
    data = {
        "all_products": products,
        "all_category": category,
    }
    return render(request, 'App_shop/index.html', data)
