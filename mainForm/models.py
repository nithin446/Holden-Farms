from django.db import models
from django.utils import timezone

class PigEntry(models.Model):
    entry_date = models.DateTimeField(
        #default = timezone.now
    )
    number_of_pigs = models.IntegerField()
    room_number = models.IntegerField()
    farm = models.ForeignKey('auth.User')
    week_of_year = models.IntegerField()
    def __str__(self):
        return "\nFarm: "+self.farm.username+"\nWeek: "+str(self.week_of_year)+"\nDate: "+self.entry_date.strftime("%Y-%m-%d %H:%M:%S")+"\nPigs: "+str(self.number_of_pigs)


    """author = models.ForeignKey('auth.User')
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