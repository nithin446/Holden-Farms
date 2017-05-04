from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class PigEntry(models.Model):
    """
    The model to store all the pig entry amounts
    Stores an entry date, the number of pigs for that date, and the farm associated with the entry
    """
    entry_date = models.DateTimeField(
        #default = timezone.now
    )
    number_of_pigs = models.IntegerField()
    #flow = models.ForeignKey('Flow', null=True)
    farm = models.ForeignKey(User)
    def __str__(self):
        return "\nFarm: "+self.farm.username+"\nDate: "+self.entry_date.strftime("%Y-%m-%d %H:%M:%S")+"\nPigs: "+str(self.number_of_pigs)

class Flow(models.Model):
    """
    Stores the flow data which ends up just being a name and abbreviation
    """
    abbreviation = models.CharField(max_length=5, default="aaa")
    name = models.CharField(max_length=100, default="aaa")

    def __str__(self):
        return self.abbreviation

class Profile(models.Model):
    """
    An extension of the built in user model so that a farm can have a flow tied to it
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    flow = models.ForeignKey('Flow', null=True)

"""
Creation and save events for the extended user profile class
"""
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
