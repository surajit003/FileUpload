from django.db.models.signals import post_save
from django.dispatch import receiver

from upload.models import Upload


@receiver(post_save, sender=Upload)
def create_profile1(sender, instance, created, **kwargs):
    if created:
        #do something
