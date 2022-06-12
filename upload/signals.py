from django.db.models.signals import post_save
from django.dispatch import receiver

from upload.models import Upload


@receiver(post_save, sender=Upload)
def process_file(sender, instance, created, **kwargs):
    if created:
        #do something
        pass
