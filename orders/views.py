from cart.cart import Cart
from django.shortcuts import render
from .forms import OrderCreateForm
from .models import OrderItem


# Create your views here.
# view to handle the form and create a new order
def order_create(request):
    cart = Cart(request)  # obtain the current cart from the session
    form = OrderCreateForm() # ! added this statment
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        # Validates the data sent in the request
        if form.is_valid():
            # create a new order in the database
            order = form.save()
            # iterate over the cart items and create an OrderItem for each of them
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity'],
                )
            # clear the cart
            cart.clear()
            # return a response after clearing the cart
            return render(request, 'orders/order/created.html', {'order': order})
        else:
            form = OrderCreateForm()
    # ! return statment is beneath if request.methnd == 'POST': and not second if statment at line 15
    return render(request, 'orders/order/create.html', {'cart': cart, 'form': form})
