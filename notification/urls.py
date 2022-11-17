from django.urls import path
from notification.views import ShowAllNotification, ArchiveNotifications

urlpatterns = [
    path('', ShowAllNotification, name='show-notification'),
    path('modify/<noti_id>', ArchiveNotifications, name='archive-notification'),


]
