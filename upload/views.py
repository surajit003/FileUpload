from django.shortcuts import render

# Create your views here.

class UploadView(CreateView):
    model = Upload
    fields = ("file_name", "file", "description")
    template_name = "upload/upload.html"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)