from django.db import models
from Profile.models import User,Profile
import datetime
import django.utils.timezone

# Create your models here.
class Message(models.Model):
    subject = models.CharField(max_length= 40,blank=True)
    body = models.TextField(max_length=1000,default="Enter your message here")
    sender = models.ForeignKey(User,on_delete=False, default="",related_name="sender")
    receiver = models.ForeignKey(Profile,on_delete=False, default="",related_name="receiver")
    time_sent = models.DateTimeField(default = django.utils.timezone.now)

    def __str__(self):
        return str(self.sender) + "<>"": " + str(self.receiver)+ ": "+ str(self.subject) + " Sent:"+str(self.time_sent)
