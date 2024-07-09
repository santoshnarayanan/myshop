implement the product_list view to list all products and the product_detail
view to display a single product. You will allow filtering products by category in the product_list
view using the category_slug parameter. You will implement a shopping cart using sessions and you
will build the cart_detail view to display the cart items. You will create the cart_add view to add
products to the cart and update quantities, and the cart_remove view to remove products from the
cart. You will implement the cart template context processor to display the number of cart items and
total cost on the site header. You will also create the order_create view to place orders, and you will
use Celery to implement the order_created asynchronous task that sends out an email confirmation
to clients when they place an order.
