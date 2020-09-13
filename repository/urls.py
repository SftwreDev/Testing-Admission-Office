from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import (
    FileList,
    delete_file
)

app_name = 'documents'
urlpatterns = [
    path("file-list-page/", FileList, name='list_of_files'),
    path("delete-file/<int:pk>/", delete_file, name='delete_file'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)