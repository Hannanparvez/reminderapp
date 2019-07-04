from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

def signin(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect("/"+request.user.username)
    
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            # messages.success(request,f"Welcome {user.username} ")
            return redirect("/"+request.user.username)

        else:
            messages.error(request,"Invalid credentials")
            return redirect('signin')


    else:
         return render(request,'accounts/signin.html')


def signup(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect("/"+request.user.username)
    
    if request.method=="POST":
        # getvalues from form
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=first_name + last_name 
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']
 
        if password==password2:
            if User.objects.filter(username=username).exists():
                messages.error(request,'That username is already taken')
                return redirect('signup')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,'That email is already taken')
                    return redirect('signup')
                
                else:
                    user=User.objects.create_user(email=email,first_name=first_name,last_name=last_name ,
                    username=username,password=password,)
                    user.save()
                    auth.login(request,user)
                    # messages.success(request,'You are registered ,you can now login')
                    return HttpResponseRedirect("/"+request.user.username)

        else:
            messages.error(request,'Passwords do not match')
            return redirect('signup')
    else:
         return render(request,'accounts/signup.html')


# Create your views here.
