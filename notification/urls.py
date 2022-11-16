from django.urls import path
from notification.views import ShowNotification, ArchiveNotifications

urlpatterns = [
    path('', ShowNotification, name='show-notification'),
    path('modify/<archive_id>', ArchiveNotifications, name='archive-notification'),


]
