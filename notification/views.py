from django.shortcuts import render, redirect
from notification.models import Notification

def ShowAllNotification(request):
    user = request.user
   
    notifications = Notification.objects.filter(user=user, archive__in=[0,1])
    
    noti_count = Notification.objects.filter(user=user, is_seen = False).count()

    print(noti_count)
    
    
    for i in notifications:
        i.bgClass = 'bg-light' if(i.is_seen == False) else ''
        
        
    
    context = {
        'notifications': notifications,
        'noti_count' : noti_count,
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
        change.is_seen = True
        change.save()
    except:
        raise(Exception)
        
        
    return redirect('show-notification')


    



