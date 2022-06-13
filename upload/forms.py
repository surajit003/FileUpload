from django import forms

from upload.models import Upload


class UploadForm(forms.ModelForm):
    class Meta:
        model = Upload
        fields = ("file_name", "file", "description", "entity")

