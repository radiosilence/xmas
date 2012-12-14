from django.shortcuts import render, get_object_or_404
from xmas.models import Card

def card(request, uuid):
    card = get_object_or_404(Card, uuid=uuid)

    if not request.user.is_staff:
        card.viewed = True
        card.save()

    return render(request, 'card.html', {
        'card': card
    })