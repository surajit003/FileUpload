from django.db import models
from django_fsm import FSMField
from django_fsm import transition


class Upload(models.Model):
    STATUS = (
        ("PENDING", "PENDING"),
        ("PROCESSING", "PROCESSING"),
        ("COMPLETED", "COMPLETED"),
    )
    file_name = models.CharField(max_length=100)
    file = models.FileField(upload_to="uploads/")
    uploaded_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField(null=True, blank=True)
    status = FSMField(choices=STATUS, default='pending', protected=True)

    def __str__(self):
        return f"{self.file_name}"

    @transition(field=status, source='pending', target='processing')
    def change_status_to_processing(self):
        return "File Status has been changed from PENDING to PROCESSING"

    @transition(field=status, source='processing', target='completed')
    def change_status_to_completed(self):
        return "File Status has been changed from PROCESSING to COMPLETED"


class Product(models.Model):
    name = models.CharField(max_length=100)
    sku = models.CharField(max_length=100,unique=True, db_index=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        ordering = ['-created_at']
