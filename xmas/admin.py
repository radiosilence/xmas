from django.contrib import admin
from xmas.models import Card

admin.site.register(Card, admin.ModelAdmin)