from django.shortcuts import render

def card(request, id=None):
    return render(request, 'card.html', {})