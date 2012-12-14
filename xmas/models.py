from django.db import models
from django.core.urlresolvers import reverse
from django_extensions.db.fields import UUIDField


class Card(models.Model):
    uuid = UUIDField(primary_key=True)
    recipient = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    sent = models.BooleanField()

    def get_absolute_url(self):
        return reverse('card', kwargs={
            'uuid': self.uuid,
        })
    def __unicode__(self):
        return u'{recipient} ({uuid})'.format(**self.__dict__)
