from django.shortcuts import render ,redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Room,Topic,message
from .forms import RoomForm,CustomUserForm


# Create your views here.
from django.http import HttpResponse
# rooms=[
#     {'id':1,'name':'Django bootcamp!'},
#     {'id':2,'name':'frontend dev!'},
#     {'id':3,'name':'python learning!'}
# ]

def loginPage(request):
    page='login'
    if request.user.is_authenticated:
        return redirect ('home')
    
    
    if request.method=='POST':
       username=request.POST.get('username').lower()
       password=request.POST.get('password')
       
       try:
           user=User.objects.get(username=username)
           
       except:
           messages.error(request,'User does not exists')
            
       user=authenticate(request,username=username,password=password)
       
       if user is not None:
           login(request,user)
           return redirect('home')   
       else:
           messages.error(request,'Username or Password does not exist')
              
    context={'page':page}
    return render(request,'base/login_form.html',context)

def logoutPage(request):
    logout(request)
    return redirect('home')

def registerPage(request):
    page='register'
    form=UserCreationForm()
    
    if request.method == 'POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.username=user.username.lower()
            user.save()
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'An Error occurred during registration!')
    
    
    
    context={'page':page,'form':form}
    return render(request,'base/login_form.html',context)


def home(request):
    q=request.GET.get('q') if request.GET.get('q')!=None else ''
        
    rooms=Room.objects.filter(Q(topic__name__icontains=q) |
                              Q(name__icontains=q) |
                              Q(description__icontains=q)
                              
                              ) #for searching a topic,name,description.. name 
    topics=Topic.objects.all()
    
    room_count=rooms.count()
    room_messages=message.objects.filter(Q(room__topic__name__icontains=q))
    
    
    context={'rooms':rooms,'topics':topics,'room_count':room_count,'room_messages':room_messages}
    return render(request,'base/home.html',context)

def room(request,pk):
    room=Room.objects.get(id=pk)
    room_messages = room.message_set.all()
    participants=room.participants.all()
    
    if request.method == 'POST':
        Message=message.objects.create(
            user=request.user,
            room=room,
            body=request.POST.get('body')
        )
        room.participants.add(request.user)
        return redirect('room',pk=room.id)
    
    context={'room':room,'room_messages':room_messages,'participants':participants}        
    return render(request,'base/room.html',context)

def userProfile(request,pk):
    user=User.objects.get(id=pk)
    rooms=user.room_set.all() #to get rooms of specific user
    room_messages=user.message_set.all()
    topics=Topic.objects.all()
    context={'user':user,'rooms':rooms,'room_messages':room_messages,'topics':topics}
    return render(request,'base/profile.html',context)


@login_required(login_url='/login')
def createRoom(request):
    form=RoomForm()
    topics=Topic.objects.all()
    if request.method=='POST':
        topic_name=request.POST.get('topic')
        topic,created=Topic.objects.get_or_create(name=topic_name)
        Room.objects.create(
            host=request.user,
            topic=topic,
            name=request.POST.get('name'),
            description=request.POST.get('description'),
        )
        return redirect('home')
    
    context={'form':form ,'topics':topics}
    return render(request,'base/room_form.html',context)

@login_required(login_url='/login')
def updateRoom(request,pk):
    room =Room.objects.get(id=pk)
    form=RoomForm(instance=room)
    topics=Topic.objects.all()
    
    if request.user!=room.host:
        return HttpResponse('You are not allowed here') 
    if request.method=='POST':
        form=RoomForm(request.POST,instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    context={'form':form ,'topics':topics}
    return render(request,'base/room_form.html',context)

@login_required(login_url='login')
def deleteRoom(request,pk):
    room=Room.objects.get(id=pk)
    
    if request.user!=room.host:
        return HttpResponse('You are not allowed here') 
    
    if request.method=='POST':
        room.delete()
        return redirect('home')
    
    return render(request,'base/delete.html',{'obj':room})


@login_required(login_url='login')
def deleteMessage(request,pk):
    Message=message.objects.get(id=pk)
    
    if request.user != Message.user:
        return HttpResponse('You are not allowed here') 
    
    if request.method=='POST':
        Message.delete()
        return redirect('home')
    
    return render(request,'base/delete.html',{'obj':Message})

@login_required(login_url='login')
def updateUser(request,pk):
    user = User.objects.get(id=pk)

    if request.method == "POST":
       form=CustomUserForm(request.POST,instance=user)
       if form.is_valid():
           form.save()
           return redirect('user-profile',pk=user.id)
    else:
       form= CustomUserForm(instance=user)     
    
    return render(request,'base/update_user.html',{'user':user,'form':form})
    