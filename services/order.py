from django.db import transaction
from db.models import Order, Ticket, User


def create_order(tickets, username, date=None):
    with transaction.atomic():
        user = User.objects.get(username=username)

        order = Order(user=user)

        if date:
            order.created_at = date

        order.save()

        for t in tickets:
            Ticket.objects.create(
                order=order,
                row=t["row"],
                seat=t["seat"],
                movie_session_id=t["movie_session"]
            )

    return order


def get_orders(username=None):
    if username:
        return Order.objects.filter(user__username=username)
    return Order.objects.all()
