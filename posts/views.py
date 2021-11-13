"""Post Views"""
#Django
from django import views
from django.contrib.auth import models
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import request
from django.shortcuts import render,redirect,HttpResponseRedirect
from django.views.generic import ListView, DetailView,CreateView,UpdateView
from django.views import View
from django.urls.base import reverse_lazy,reverse
#Forms
from posts.forms import PostForm

#Models
from posts.models import Post, Like, Comment



# Create your views here.
class UpdateComment(LoginRequiredMixin,UpdateView):
    """Update a comment"""
    template_name='posts/update_comment.html'
    model=Comment
    fields={'comment'}
    context_object_name='comment'

    def post(self, request, *args, **kwargs):
        print(request.POST)
        if request.POST.get("comment_id",False):
            return redirect("posts:update_comment",request.POST["comment_id"])
        return super().post(request, *args, **kwargs)
            
    def get_success_url(self):
        post_id=self.object.post.pk
        return reverse_lazy('posts:detail',kwargs={'pk':post_id})
    

class DeleteComment(LoginRequiredMixin,View):
    """Delete a Comment"""
    def post(self,request,*args,**kwargs):
        Comment.objects.get(pk= self.request.POST['comment_id']).delete()
        return redirect('posts:detail',request.POST['post_id'])

class PostComment(LoginRequiredMixin,View):
    def post(self, request, *args, **kwargs):
        if request.POST['comment'].strip()!='':
            comment = Comment(comment=request.POST['comment'],user_id=request.POST['user_id'],post_id=request.POST['post_id'])
            comment.save()
            return redirect('posts:detail',request.POST['post_id'])
        

class UpdatePost(LoginRequiredMixin,UpdateView):
    """Update a post"""
    template_name='posts/update.html'
    model=Post
    fields={'title','description'}
    context_object_name='post'

    def post(self, request, *args, **kwargs):
        if request.POST.get("post_id",False):
            return redirect("posts:update",request.POST["post_id"])
        return super().post(request, *args, **kwargs)
 
    def get_success_url(self):
        """Return to users profile"""
        username=self.object.user.username
        return reverse_lazy('users:detail',kwargs={'username':username})


class DeletePost(View,LoginRequiredMixin):
    """Delete Post"""
    def post(self,request,*args,**kwargs):
        Post.objects.get(pk=request.POST['post_id']).delete()
        return redirect('users:detail',request.POST['username'])


class PostLike(View,LoginRequiredMixin):
    """Update Likes"""
    def post(self, request, *args, **kwargs):
        """Logic for the POST method"""
        post=Post.objects.get(id = request.POST['post_id'])
        user= User.objects.get(id=request.user.pk)
        post_id= post.pk
        user_id= user.pk
        profile_id=user.profile.pk
        like= Like.objects.filter(post_id=post_id).filter(user_id=user_id).filter(profile_id=profile_id)
        if len(like)==0:
            new_like= Like(user_id=user_id,profile_id=profile_id,post_id=post_id)
            post.likes+=1
            post.save()
            new_like.save()
        else:
            like.delete()
            post.likes-=1
            post.save()
        
        return redirect('posts:detail',post_id)



class PostsFeedView(LoginRequiredMixin,ListView):
    """Return All Published posts"""
    template_name='posts/feed.html'
    Model=Post
    queryset=Post.objects.all()
    ordering=('-created')
    paginate_by=30
    context_object_name='posts'
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(PostsFeedView, self).get_context_data(**kwargs)
        # Get the blog from id and add it to the context
        context['ubication'] = 'feed'
        return context

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
