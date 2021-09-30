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
    path(
        route='posts/update/<int:pk>/',
        view=views.UpdatePost.as_view(),
        name='update'),
    path(
        route='posts/comment/',
        view=views.PostComment.as_view(),
        name='comment'),
    path(
        route='posts/comment/delete/',
        view=views.DeleteComment.as_view(),
        name='delete_comment'),
    path(
        route='posts/comment/update/<int:pk>/',
        view=views.UpdateComment.as_view(),
        name='update_comment'),

]