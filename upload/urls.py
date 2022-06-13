from django.urls import path

from upload import views

urlpatterns = [
    path(
        "uploads/",
        views.UploadCreateView.as_view(),
        name="upload_create",
    ),
    path(
        "upload/<int:pk>/",
        views.UploadDetailView.as_view(),
        name="upload_detail",
    ),
]
