from django.urls import path

from upload import views

urlpatterns = [
    path("uploads/",
         views.UploadView.as_view(),
         name="uploads",
         ),
]
