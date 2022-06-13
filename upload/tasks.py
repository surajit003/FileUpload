import csv

from upload.models import Upload, Product


def parse_file(upload_id):
    """
    Parse the file and return the data
    """
    upload = Upload.objects.get(id=upload_id)
    upload.change_status_to_processing()
    upload.save()

    with open(upload.file.path, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                product = Product(
                    name=row["name"],
                    sku=row["sku"],
                    price=row["price"],
                    description=row["description"],
                )
            except KeyError as exc:
                upload.append_error(exc)
                pass
            product.save()
    upload.change_status_to_completed()
    upload.save()


