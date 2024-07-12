from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm


# Create your views here.
def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    # filter the QuerySet with available=True to retrieve only available products
    products = Product.objects.filter(available=True)
    if category_slug:
        # optional category_slug parameter to optionally filter products by a given category
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'shop/product/list.html',
                  {'category': category, 'categories': categories, 'products': products}
                  )


def product_detail(request, id, slug):
    # retrieve and display a single product
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/product/detail.html' ,
                  {'product': product, 'cart_product_form': cart_product_form})

