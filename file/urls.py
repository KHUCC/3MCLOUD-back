from . import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers


urlpatterns = [
    path("upload/<str:folder_id>", views.uploadFile, name="uploadFile"),
    path("<int:file_id>/download/", views.downloadFile, name="downloadFile"),
    path("", views.listFile, name="listFile"),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
