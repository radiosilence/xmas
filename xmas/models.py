from django.db import models
from django.core.urlresolvers import reverse
from django.dispatch import receiver
from django_extensions.db.fields import UUIDField
from django.db.models.signals import pre_save
from django.core.mail import send_mail

class Card(models.Model):
    uuid = UUIDField(primary_key=True)
    recipient = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    sent = models.BooleanField()
    viewed = models.BooleanField()
    draft = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse('card', kwargs={
            'uuid': self.uuid,
        })

    def send(self):
        self.sent = True

    def __unicode__(self):
        return u'{recipient} ({uuid})'.format(**self.__dict__)

@receiver(pre_save, sender=Card)
def send_card(sender, instance, **kwargs):
    if not instance.draft:
        instance.send()

