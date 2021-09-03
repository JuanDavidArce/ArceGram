"""User views"""

#Django
from users.models import Profile
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

#Models
from django.contrib.auth.models import User

#Exeption
from django.db.utils import IntegrityError

# Create your views here.

def update_profile(request):
    """Update a user's profile view"""
    return render(request,'users/update_profile.html')

def login_view(request):
    """Login view"""
    if request.method=='POST':
        username= request.POST['username']
        password=request.POST['password']
        
        user=authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return redirect('feed')
        else:
            return render(request,'users/login.html',{'error': 'Invalid username and password'})
       
    return render(request,'users/login.html')

@login_required
def logout_view(request):
    """Logout a user"""
    logout(request)
    return redirect('login')

def signup_view(request):
    if request.method== 'POST':
        username= request.POST['username']
        passwd=request.POST['passwd']
        passwd_confirmation= request.POST['passwd_confirmation']
        if passwd!= passwd_confirmation:
            return render(request,'users/signup.html',{'error': 'Password confirmation does not match'})
        else:
            try:
                user=User.objects.create_user(username=username,password=passwd)
            except IntegrityError:
                return render(request,'users/signup.html',{'error': 'Username is already in user'})
            user.first_name=request.POST['first_name']
            user.last_name=request.POST['last_name']
            user.email=request.POST['email']
            user.save()

            profile=Profile(user=user)
            profile.save()
            return redirect('login')

    return render(request,'users/signup.html')