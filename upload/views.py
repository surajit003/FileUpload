from django.views.generic import CreateView, DetailView

from upload.forms import UploadForm
from upload.models import Upload
from django.shortcuts import reverse


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
