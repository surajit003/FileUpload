from django.db import models


class Upload(models.Model):
    file_name = models.CharField(max_length=100)
    file = models.FileField(upload_to="uploads/")
    uploaded_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

