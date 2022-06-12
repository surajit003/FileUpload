from django.db.models.signals import post_save
from django.dispatch import receiver

from upload.models import Upload

from upload.tasks import parse_file

import django_rq

queue = django_rq.get_queue('default')


@receiver(post_save, sender=Upload)
def process_file(sender, instance, created, **kwargs):
    if created:
        queue.enqueue(parse_file, instance.id)


