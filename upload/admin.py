from django.contrib import admin

from upload import models


# Register your models here.


@admin.register(models.Upload)
class FileUploadAdmin(admin.ModelAdmin):
    list_display = ("file_name", "uploaded_at", "status", "description", "entity")
    search_fields = ("file_name",)
    readonly_fields = ("status",)


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "sku",
        "price",
        "description",
        "active",
    )
    search_fields = ("name", "sku")
    readonly_fields = ("created_at", "updated_at")
