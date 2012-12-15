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
        if not self.sent:
            send_mail('Oh my! A Christmas card? Wow!',
                ('It appears that I\'ve sent you a Christmas card. Take a deep '
                + 'breath, let that sink in for a moment, then click here to have '
                + 'a looksie: \n\n'
                + 'http://blackflags.co.uk{}'
                + '\n\n'
                + 'Toodle pip!'
                ).format(
                    self.get_absolute_url()
                ),
                'James Cleveland <jc@blackflags.co.uk>',
                [self.email],
                fail_silently=False
            )

    def __unicode__(self):
        return u'{recipient} ({uuid})'.format(**self.__dict__)

@receiver(pre_save, sender=Card)
def send_card(sender, instance, **kwargs):
    if not instance.draft:
        instance.send()
