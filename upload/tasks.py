import csv

from django.core.exceptions import ValidationError
from django.db import IntegrityError


from upload.models import Upload, Product


def parse_file(upload_id):
    """
    Parse the file and create the products.
    """
    upload = Upload.objects.get(id=upload_id)
    upload.change_status_to_processing()
    upload.save()

    with open(upload.file.path, "r", encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for count, row in enumerate(reader):
            try:
                if upload.entity == "PRODUCT":
                    # this can be changed to bulk_create or bulk_update
                    product, _ = Product.objects.update_or_create(
                        sku=row["sku"],
                        defaults={
                            "name": row["name"],
                            "price": row["price"],
                            "description": row["description"],
                        },
                    )
            except (ValidationError,IntegrityError) as exc:
                upload.append_error({"line_number": count, "error": str(exc)})
                pass
            product.save()
    upload.change_status_to_completed()
    upload.save()
