from django.contrib.auth.models import User
from django.db import transaction
import datetime

from db.models import Order, Ticket


def create_order(tickets: list[dict], username: str| None, data: datetime) -> None:
    with transaction.atomic():
        user = User.objects.get(username=username)
        order = Order.objects.create(user=user, created_at=data)

        for ticket in tickets:
            Ticket.objects.create(
                order=order,
                row=ticket["row"],
                seat=ticket["seat"],
                movie_session_id=ticket["movie_session"]
            )


