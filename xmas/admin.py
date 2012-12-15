from django.contrib import admin
from xmas.models import Card

class CardAdmin(admin.ModelAdmin):
    list_display = ['recipient', 'email', 'sent', 'viewed', 'draft']
    list_editable = ['draft']

admin.site.register(Card, CardAdmin)
