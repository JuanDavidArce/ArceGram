"""Posts URLs"""
#Django
from django.urls import path

#Views
from posts import views

urlpatterns=[
    path(
        route='',
        view=views.PostsFeedView.as_view(), 
        name='feed'),

    path(
        route='post/<int:pk>',
        view=views.PostDetailView.as_view(), 
        name='detail'),

    path(
        route='posts/new/',
        view=views.CreatePostView.as_view(),
        name='create'),

    path(
        route='posts/like/',
        view=views.PostLike.as_view(),
        name='like'),

    path(
        route='posts/delete/',
        view=views.DeletePost.as_view(),
        name='delete'),

]