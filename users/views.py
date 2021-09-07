"""User views"""

#Django
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from django.urls import reverse

#Models
from django.contrib.auth.models import User
from posts.models import Post
#Forms
from users.forms import ProfileForm, SignupForm


class UserDetailView(LoginRequiredMixin,DetailView):
    """User template view"""
    template_name='users/detail.html'
    slug_field='username'
    slug_url_kwarg='username'
    queryset=User.objects.all()
    context_object_name='user'
    def get_context_data(self, **kwargs):
        """Add users posts to context"""
        context=super().get_context_data(**kwargs)
        user=self.get_object()
        context['posts']=Post.objects.filter(user=user).order_by('-created')
        return context



# Create your views here.
@login_required
def update_profile(request):
    """Update a user's profile view"""
    profile=request.user.profile

    if request.method=='POST':
        form=ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            data= form.cleaned_data
            profile.website=data['website']
            profile.phone_number=data['phone_number']
            profile.biography=data['biography']
            profile.picture=data['picture']
            profile.save()
            url=reverse('users:detail',kwargs={'username':request.user.username})
            return redirect(url)
    else:
        form=ProfileForm()

    return render(request,'users/update_profile.html',
    context={'profile':profile,'user':request.user,'form':form})

def login_view(request):
    """Login view"""
    if request.method=='POST':
        username= request.POST['username']
        password=request.POST['password']
        
        user=authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return redirect('posts:feed')
        else:
            return render(request,'users/login.html',{'error': 'Invalid username and password'})
       
    return render(request,'users/login.html')

@login_required
def logout_view(request):
    """Logout a user"""
    logout(request)
    return redirect('users:login')

def signup_view(request):
    if request.method== 'POST':
        form= SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('users:login')
    else:
        form=SignupForm()


    return render(request,'users/signup.html',context={'form':form})