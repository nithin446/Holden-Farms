from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class PigEntry(models.Model):
    entry_date = models.DateTimeField(
        #default = timezone.now
    )
    number_of_pigs = models.IntegerField()
    #flow = models.ForeignKey('Flow', null=True)
    farm = models.ForeignKey(User)
    def __str__(self):
        return "\nFarm: "+self.farm.username+"\nDate: "+self.entry_date.strftime("%Y-%m-%d %H:%M:%S")+"\nPigs: "+str(self.number_of_pigs)

class Flow(models.Model):
    abbreviation = models.CharField(max_length=5, default="aaa")
    name = models.CharField(max_length=100, default="aaa")

    def __str__(self):
        return self.abbreviation

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    flow = models.ForeignKey('Flow', null=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
"""
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    test = models.TextField()
    created_date = models.DateTimeField(
        default = timezone.now
    )
    published_date = models.DateTimeField(
        blank = True, null = True
    )
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title"""