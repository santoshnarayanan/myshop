from celery import shared_task
from django.core.mail import send_mail
from .models import Order


@shared_task
def order_created(order):
    """
    Task to send an e-mail notification when an order is successfully created
    """
    order = Order.objects.get(id=order)
    subject = f'Order nr.{order.id}'
    message = (
        f'Dear {order.first_name} {order.last_name},\n'
        f'Your order has been created.\n'
        f'Your order Id: {order.id}\n'
    )
    mail_sent = send_mail(subject, message, 'admin@myshop.com', [order.email])
    return mail_sent
