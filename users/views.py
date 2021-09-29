"""User views"""

#Django
from django.db.models.base import Model
from users.models import Profile, Follower
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls.base import reverse_lazy,reverse
from django.views.generic import DetailView,FormView,UpdateView,DeleteView,ListView
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views

#Models
from django.contrib.auth.models import User
from posts.models import Post
#Forms
from users.forms import  SignupForm

class UserFollowing(LoginRequiredMixin,ListView):
    """Return All Following Users"""
    template_name= 'users/following.html'
    Model= Follower
    context_object_name='following'
    def get_queryset(self):
        return Follower.objects.filter(follower_id=self.request.user.pk)
    

class UserFollowers(LoginRequiredMixin,ListView):
    """Return All Followers"""
    template_name='users/followers.html'
    Model=Follower
    context_object_name='followers'
    def get_queryset(self):
        return Follower.objects.filter(user_id=self.request.user.pk)
    
class DeleteUser(DeleteView,LoginRequiredMixin):
    """Delete Post"""
    model=User
    success_url= reverse_lazy('users:login')

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
    def post(self, request, *args, **kwargs):
        user_to_follow_id = int(request.POST['user_to_follow'])
        user_follower_id = int(request.POST['user_follower'])
        user= User.objects.get(id= user_to_follow_id)
        already_following = Follower.objects.filter(user_id=user_to_follow_id).filter(follower_id=user_follower_id)
        if len(already_following)==0:
            new_follower = Follower(user_id= user_to_follow_id,follower_id=user_follower_id, profile_id=user.profile.pk)
            new_follower.save()
        else:
            already_following.delete()
        return redirect('users:detail',user.username)


class SignupView(FormView):
    """Users signup view"""
    template_name='users/signup.html'
    form_class=SignupForm
    success_url=reverse_lazy('users:login')

    def form_valid(self, form):
        """Save form data"""
        form.save()
        return super().form_valid(form)


class UpdateProfileView(LoginRequiredMixin,UpdateView):
    """Update profile view"""
    template_name='users/update_profile.html'
    model=Profile
    fields=['website','biography','phone_number','picture']

    def get_object(self):
        """Return users profile"""
        return self.request.user.profile
    def get_success_url(self):
        """Return to users profile"""
        username=self.object.user.username
        return reverse('users:detail',kwargs={'username':username})
        


class LoginView(auth_views.LoginView):
    """Login view"""
    template_name='users/login.html'



class LogoutView(LoginRequiredMixin,auth_views.LogoutView):
    """Logout View"""
    template_name='users/logout.html'