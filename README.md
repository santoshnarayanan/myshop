Summary - 
======================
1. Create a product catalog
2. Build a shopping cart using Django sessions
3. Create custom template context processors
4. Manage customer orders
5. Configure Celery in your project with RabbitMQ as a message broker
6. Send asynchronous notifications to customers using Celery
7. Monitor Celery using Flower

Implementation
=======================

1. Implement the product_list view to list all products and the product_detail
view to display a single product. 
2. Allow filtering products by category in the product_list
view using the category_slug parameter. 
3. Implement a shopping cart using sessions and you
will build the cart_detail view to display the cart items. 
4. Create the cart_add view to add
products to the cart and update quantities, and the cart_remove view to remove products from the
cart. 
5. Implement the cart template context processor to display the number of cart items and
total cost on the site header. 
6. Create the order_create view to place orders, and 
use Celery to implement the order_created asynchronous task that sends out an email confirmation
to clients when they place an order.