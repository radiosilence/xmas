from django.core.management.base import BaseCommand, CommandError
from xmas.models import Card

class Command(BaseCommand):
    def handle(self, *args, **options):
        for card in Card.objects.filter(draft=False, sent=False):
            print "Sending {}".format(card)
            card.send()
