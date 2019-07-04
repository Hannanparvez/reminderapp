from django.contrib import admin
from .models import Reminder

# Register your models here.
class ReminderAdmin(admin.ModelAdmin):
    list_display=('id','reminderdescription','reminder_user','reminderstatus')
    list_display_links=('id','reminder_user')
    list_per_page=25

admin.site.register(Reminder,ReminderAdmin)