"""Post Views"""
#Django
from django.db.models.base import Model
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.generic.detail import DetailView

#Forms
from posts.forms import PostForm
#Models
from posts.models import Post


# Create your views here.

class PostsFeedView(LoginRequiredMixin,ListView):
    """Return All Published posts"""
    template_name='posts/feed.html'
    Model=Post
    queryset=Post.objects.all()
    ordering=('-created')
    paginate_by=2
    context_object_name='posts'

class PostDetailView(LoginRequiredMixin,DetailView):
    template_name='posts/detail.html'
    queryset= Post.objects.all()
    context_object_name='post'

@login_required
def create_post(request):
    """create new post view"""
    if request.method=='POST':
        form=PostForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('posts:feed')
    else:
        form=PostForm()

    return render(request=request, template_name='posts/new.html',context={
        'form':form,
        'user':request.user,
        'profile':request.user.profile
    })