from upload.models import Upload


def parse_file(upload_id):
    """
    Parse the file and return the data
    """
    upload = Upload.objects.get(id=upload_id)

