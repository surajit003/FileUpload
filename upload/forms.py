from django import forms

from upload.models import Upload


class FileUploadForm(forms.ModelForm):
    model = Upload
    fields = ("file_name", "file", "description")

