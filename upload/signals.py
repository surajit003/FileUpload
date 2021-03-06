import django_rq

from django.db.models.signals import post_save
from django.dispatch import receiver

from upload.models import Upload
from upload.tasks import parse_file
from upload.utils import extract_header
from upload.utils import validate_compulsory_header

queue = django_rq.get_queue("default")


@receiver(post_save, sender=Upload)
def process_file(sender, instance, created, **kwargs):
    if created:
        header = extract_header(instance.file.path)
        if validate_compulsory_header("product", header):
            queue.enqueue(parse_file, instance.id)
        else:
            instance.append_error(
                {"line_number": 0, "error": "Missing Compulsory Headers"}
            )
            instance.save()
