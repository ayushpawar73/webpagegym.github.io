from django.shortcuts import render
from django.shortcuts import redirect , render
from .models import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as auth_login

# Create your views here.
def home(request):
    return render(request,'index.html')

def bil(request):
    return render(request,'bills.html')
def service(request):
    return render(request,'services.html')
def about(request):
    return render(request,'about_as.html')

#def con(request):
    #return render(request,'contact_us.html')


def con(request):
      if request.method =='POST':
        x=request.POST['fname']
        y=request.POST['mail_id']
        z=request.POST['phno']
        w=request.POST['msg']
        contacts.objects.create(name=x,email=y,phone_no=z,Message=w)
        
        return render(request,'contact_us.html') 
      else :
      
       return render(request,'contact_us.html')
