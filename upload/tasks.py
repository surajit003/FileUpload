from upload.models import Upload


def parse_file(upload_id):
    """
    Parse the file and return the data
    """
    upload = Upload.objects.get(id=upload_id)
    upload.change_status_to_processing()
    upload.save()

