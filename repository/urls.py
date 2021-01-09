from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import (
    FileList,
    delete_file,
    office_file_list,
    office_file_update,
    office_file_delete
)

app_name = 'documents'
urlpatterns = [
    path("file-list-page/", FileList, name='list_of_files'),
    path("delete-file/<int:pk>/", delete_file, name='delete_file'),

    path("offfice-file-list-page/", office_file_list, name='office_file_list'),
    path("office-file-update/<int:pk>/", office_file_update, name='office_file_update'),
    path("office-file-delete/<int:pk>/", office_file_delete, name='office_file_delete'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)