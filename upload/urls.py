from django.urls import path

from uploads import views

urlpatterns = [
    path(
        r"^uploads/$",
        views.UploadView.as_view(),
        name="uploads",
    ),
]