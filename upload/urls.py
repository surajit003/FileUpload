from django.urls import path

from upload import views

urlpatterns = [
    path(
        r"^uploads/$",
        views.UploadView.as_view(),
        name="uploads",
    ),
]