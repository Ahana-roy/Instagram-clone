from django.db import models
from django.contrib.auth.models import User
# from post.models import Post

class Notification(models.Model):
    NOTIFICATION_TYPES = ((1, 'Like'), (2, 'Comment'), (3, 'Follow'))

    post = models.ForeignKey("post.Post", on_delete=models.CASCADE, related_name="notification_post", null=True, blank=True)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notification_from_user" )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notification_to_user" )
    notification_types = models.IntegerField(choices=NOTIFICATION_TYPES, null=True, blank=True)
    text_preview = models.CharField(max_length=100, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    is_seen = models.BooleanField(default=False)

    # 0--> recent unseen notifications, 1-->hidden notifications, 2-->delete notifications

    archive = models.SmallIntegerField(null=True, blank=True, default=0)




    # def __str__(self):
    #     return self.text_preview



