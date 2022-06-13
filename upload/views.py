from django.views.generic import CreateView
from django.views.generic import DetailView
from django.shortcuts import reverse

from upload.forms import UploadForm
from upload.models import Upload


class UploadCreateView(CreateView):
    model = Upload
    form = UploadForm
    fields = ("file_name", "file", "description", "entity")
    template_name = "upload/upload.html"
    success_url = "/upload/"

    def get_success_url(self):
        return reverse("upload_detail", kwargs={"pk": self.object.pk})


class UploadDetailView(DetailView):
    model = Upload
    template_name = "upload/upload_detail.html"
