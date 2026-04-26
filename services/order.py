from django.db import transaction
from django.contrib.auth import get_user_model
from db.models import Order, Ticket

User = get_user_model()


@transaction.atomic
def create_order(tickets, username, date=None):
    user = User.objects.get(username=username)

    order = Order.objects.create(user=user)

    if date:
        Order.objects.filter(id=order.id).update(created_at=date)
        order.refresh_from_db()

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
