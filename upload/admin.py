from django.contrib import admin

from upload import models

# Register your models here.


@admin.register(models.Upload)
class FileUploadAdmin(admin.ModelAdmin):
    list_display = ("file_name", "uploaded_at", "status", "description")
    search_fields = ("file_name",)
    readonly_fields = ("status",)
