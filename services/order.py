from django.contrib.auth.models import User
from django.db import transaction
from django.db.models import QuerySet
from db.models import Order, Ticket


def get_orders(username: str = None) -> QuerySet:
    if username:
        return Order.objects.filter(user__username=username)
    return Order.objects.all()

def create_order(tickets: list, username: str, date=None) -> None:
    with transaction.atomic():
        user = User.objects.get(username=username)
        order = Order.objects.create(user=user, created_at=date)
        for ticket in tickets:
            Ticket.objects.create(
                order=order,
                row=ticket["row"],
                seat=ticket["seat"],
                movie_session_id=ticket["movie_session"]
            )
