# Generated by Django 4.0.5 on 2022-06-13 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("upload", "0002_product"),
    ]

    operations = [
        migrations.AddField(
            model_name="upload",
            name="error",
            field=models.JSONField(blank=True, null=True),
        ),
    ]
