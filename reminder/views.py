from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.models import User
from django.contrib import messages,auth
from .models import Reminder
from datetime import datetime


# Create your views here.
def index(request):
    return render(request,'pages/index.html')

def home(request,un):
    ag=get_object_or_404(User,username=un)
    remi=Reminder.objects.order_by('reminderdue').filter(reminder_user__exact=ag,reminderstatus=True)
    disabledremi=Reminder.objects.order_by('reminderdue').filter(reminder_user__exact=ag,reminderstatus=False)
    context={
            'Reminders':remi,
            'Disabledreminders':disabledremi,

        }
    
    if request.method=="POST":
        if "Logout" in request.POST:
            print("logout")
            auth.logout(request)
        # messages.success(request,"you are logged out successfully")
            return redirect('index')
        
        if "addReminder" in request.POST:
            status=False
            if request.POST.get('Reminder_status', False)=="on":
                status=True
            Reminder_description=request.POST['addReminder_description']
            Reminder_date=request.POST['Reminder_date']
            reminder=Reminder.objects.create(reminderdescription=Reminder_description,reminderstatus=status,reminderdue=Reminder_date , reminder_user=ag)
            reminder.save()
            messages.success(request,": Reminder Added")
        if "Delete" in request.POST:
            # print(request.POST['deleteReminder_id'])
            Reminder_id=request.POST['deleteReminder_id']
            Reminder.objects.filter(pk=Reminder_id).delete()
            messages.success(request,": Reminder Deleted")
        if "Edit" in request.POST:
            print("trying to edit")
            Reminder_description=request.POST['editReminder_description']
            Reminder_id=request.POST['Reminder_id']
            status=False
            if request.POST.get('editReminder_status', False)=="on":
                status=True
            if request.POST.get('editReminder_date', False):
                Reminder_date=request.POST['editReminder_date']
                Reminder.objects.filter(pk=Reminder_id).update(reminderdescription=Reminder_description,reminderstatus=status,reminderdue=Reminder_date )
                messages.success(request,": Reminder Edited")
            else:
                 Reminder.objects.filter(pk=Reminder_id).update(reminderdescription=Reminder_description,reminderstatus=status)
                 messages.success(request,": Reminder Edited")      
       


    if un != request.user.username:
        return redirect('signin')    
       
    if request.user.is_authenticated:
        return render(request,'pages/home.html',context)
    else:
        return render(request,'pages/index.html')

    return render(request,'pages/home.html',context)
