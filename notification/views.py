from django.shortcuts import render, redirect
from notification.models import Notification

def ShowAllNotification(request):
    user = request.user
   
    notifications = Notification.objects.filter(user=user, archive__in=[0,1])
    

    context = {
        'notifications': notifications,

    }

    return render(request, 'notifications/notification.html', context)

# def DeleteNotification(request, noti_id):
   
#     user = request.user
#     Notification.objects.filter(id=noti_id, user=user).delete()
    

#     return redirect('show-notification')



def ArchiveNotifications(request, noti_id):
    user = request.user

    print(noti_id)
    
    
    try:
        change = Notification.objects.get(id=noti_id)
        change.archive = 1
        change.save()
    except:
        raise(Exception)
        
        
    return redirect('show-notification')


    



