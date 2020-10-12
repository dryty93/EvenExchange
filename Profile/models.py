from django.db import models
from django.contrib.auth.models import User
from AOI.models import User
#saves updates to pf
from django.db.models.signals import post_save
from django.template.defaultfilters import slugify

#receives info from signals
from django.dispatch import receiver


class Profile(models.Model):


    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    name = models.CharField(max_length=30)
    bio = models.TextField(blank=True, default="Don't Be Shy.")
    location = models.CharField(max_length=250, blank=True, default="Cloud")
    career = models.CharField(max_length=250, blank=True)
    chi = models.IntegerField(default = 1000)
    slug = models.SlugField(default=slugify(user), max_length=100)



 #   areas_of_interest = models.OneToOneField(AreasOfInterest, on_delete=False)

    def slugger(self):
        return slugify(self.name)

    def __str__(self):
        return  f'{self.user}'



@receiver(post_save, sender=User,dispatch_uid='save_new_user_profile')
def create_user_profile(sender,instance,created, **kwargs):
    if created:

       profile = Profile.objects.create(user=instance)
       print(profile)
       profile.slug = slugify(str(profile.name))
       profile.save()


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


