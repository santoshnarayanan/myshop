from decimal import Decimal
from django.conf import settings
from shop.models import Product


# Cart class that will allow you to manage the shopping cart
class Cart:
    def __init__(self, request):
        # init cart
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, quantity=1, override_quantity=False):
        # Add product to the cart or update its quantity
        # convert the product ID into a string because Django uses JSON to serialize session data
        product_id = str(product.id)
        if product_id not in self.cart:
            # product’s price is converted from decimal into a string to serialize it
            self.cart[product_id] = {
                'quantity': 0,
                'price': str(product.price)
            }
        if override_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        # mark session as "modified" to make sure it gets saved
        self.session.modified = True

    # remove product from cart
    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    # iterate through the items contained in the cart and access the related Product instances.
    # __iter__() method will allow you to easily iterate over the items in the cart in views and templates
    def __iter__(self):
        product_ids = self.cart.keys()
        # get the product objects and add them to the cart
        products = Product.objects.filter(id__in=product_ids)
        # copy the current cart in the cart variable and add the Product instances to it.
        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product
        # iterate over the cart items, converting each item’s price back into decimal, and adding
        # a total_price attribute to each item
        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['quantity'] = item['price'] * item['quantity']
            yield item

    # Count all items in the cart
    def __len__(self):
        # return the sum of the quantities of all the cart items
        return sum(item['quantity'] for item in self.cart.values())

    # calculate the total cost of the items in the cart:
    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    # Clear cart session
    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()
