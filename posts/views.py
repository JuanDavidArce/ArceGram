"""Post Views"""
#Django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls.base import reverse_lazy
from django.shortcuts import render,redirect
from django.views.generic import ListView, DetailView,CreateView,UpdateView,RedirectView
from django.views import View
#Forms
from posts.forms import PostForm

#Models
from posts.models import Post


# Create your views here.

class PostLike(View,LoginRequiredMixin):

    def get(self, request, *args, **kwargs):
        """Logic for the GET method"""
        post=Post.objects.get(id = kwargs['idPost'])
        post.likes+=1
        post.save()
        return redirect('posts:feed')



class PostsFeedView(LoginRequiredMixin,ListView):
    """Return All Published posts"""
    template_name='posts/feed.html'
    Model=Post
    queryset=Post.objects.all()
    ordering=('-created')
    paginate_by=30
    context_object_name='posts'

class PostDetailView(LoginRequiredMixin,DetailView):
    """Return post detail"""
    template_name='posts/detail.html'
    queryset= Post.objects.all()
    context_object_name='post'


class CreatePostView(LoginRequiredMixin,CreateView):
    """Create new post view"""
    #DON'T FORGET THE VALIDATION OF A PREVIOUS LIKE
    template_name='posts/new.html'
    form_class=PostForm
    success_url=reverse_lazy('posts:feed')
    def get_context_data(self, **kwargs):
        """Add user and profile context"""
        context= super().get_context_data(**kwargs)
        context['user']=self.request.user
        context['profile']=self.request.user.profile
        return context
