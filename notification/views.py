from django.shortcuts import render, redirect
from notification.models import Notification

def ShowNotification(request):
    user = request.user
   
    notifications = Notification.objects.filter(user=user)

    context = {
        'notifications': notifications,

    }

    return render(request, 'notifications/notification.html', context)

# def DeleteNotification(request, noti_id):
   
#     user = request.user
#     Notification.objects.filter(id=noti_id, user=user).delete()
    

#     return redirect('show-notification')



def ArchiveNotifications(request, archive_id):
    user = request.user

    print(archive_id)
    if archive_id == '2':
        Notification.objects.filter(archive = archive_id, user = user).delete()
        return redirect('show-notification')

   

    



