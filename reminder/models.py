from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from datetime  import datetime


# Create your models here.
class Reminder(models.Model):
    reminderdescription=models.TextField(blank=False)
    remindertime=models.DateTimeField(default=datetime.now,blank=True)
    reminderdue=models.DateTimeField(blank=False)
    reminder_user=models.ForeignKey(User,on_delete=models.DO_NOTHING)
    reminderstatus=models.BooleanField(blank=False)
    def __str__(self):
        return self.reminderdescription