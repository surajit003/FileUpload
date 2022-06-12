from datetime import timedelta

from django.db.models.signals import post_save
from django.dispatch import receiver
from redis import Redis
from rq_scheduler import Scheduler
from upload.models import Upload

from upload.tasks import parse_file

scheduler = Scheduler(connection=Redis())


@receiver(post_save, sender=Upload)
def process_file(sender, instance, created, **kwargs):
    if created:
        scheduler.enqueue_in(timedelta(minutes=1), parse_file, instance.id)
