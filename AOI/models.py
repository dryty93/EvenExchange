from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import datetime
from django.utils.timezone import utc,now

# Create your models here.

#saves updates to pf
from django.db.models.signals import post_save

#receives info from signals
from django.dispatch import receiver


#AOI areas of interest
class AOI(models.Model):
    now = datetime.datetime.utcnow().replace(tzinfo=utc)
    name = models.CharField(max_length=300, null=False)
    author = models.ForeignKey(User,on_delete=False, default="")
    summary = models.TextField(blank=True)
    published_date = models.DateTimeField(default=timezone.now)
    thumbnail = models.ImageField(blank=True, upload_to='aoi_pics/')
    #fans = models.ForeignKey(User, related_name='fans',on_delete=None, default="")
    fans = models.ManyToManyField(User, related_name='fans')



    def __str__(self):
        return self.name



class Post(models.Model):
    title = models.CharField(max_length=1500, null=False)
    aoi = models.ForeignKey(AOI, related_name='aoi_name',on_delete=models.CASCADE,default="")
    text = models.TextField(blank=True)
    video = models.FileField( upload_to='vids', default="",blank=True)
    image = models.ImageField( upload_to='post_images', default='', blank=True)
    published_date = models.DateTimeField(default= now)
    author =  models.ForeignKey(User,on_delete=models.CASCADE, default="")
    chi_gained = models.IntegerField(blank=True, default=5)
    slug = models.SlugField(default="")

    def __str__(self):
        return self.title

class Comment(models.Model):

    author =  models.ForeignKey(User,on_delete=models.CASCADE, default="")
    post = models.ForeignKey(Post,on_delete=models.CASCADE,default="")
    text = models.TextField(blank=True)
    published_date = models.DateTimeField(default=now)
    image = models.ImageField(blank=True, upload_to='post_images')


    def __str__(self):
        return str(self.author) + ' ' + str(self.published_date)




#@receiver(post_save, sender=Profile)
#def add_user_aoi(sender,instance,created, **kwargs):
 #   if created:
  #      AOI.objects.created(Profile=instance)


#@receiver(post_save, sender=Profile)
#def save_user_aoi(sender, instance, **kwargs):
 #   instance.AOI.save()