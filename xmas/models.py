from django.db import models

class Card(models.Model):
    recipient = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    sent = models.BooleanField()
