"""Users URLs"""
#Djano
from django.urls import path

#View
from users import views


urlpatterns=[

    #Management
    path(
        route='login/',
        view=views.LoginView.as_view(),
        name='login'),

    path(
        route='logout/',
        view=views.LogoutView.as_view(),
        name='logout'),

    path(
        route='signup/',
        view=views.SignupView.as_view(),
        name='signup'),

    path(
        route='me/profile/',
        view=views.UpdateProfileView.as_view(),
        name='update_profile'),
    path(
        route='me/profile/<int:pk>',
        view=views.DeleteUser.as_view(),
        name='delete_profile'),
    path(
        route='me/profile/followers/<int:pk>',
        view=views.UserFollowers.as_view(),
        name='followers'),
    path(
        route='me/profile/following/<int:pk>',
        view=views.UserFollowing.as_view(),
        name='following'),

    path(
        route='search',
        view=views.UserSearch.as_view(),
        name='search'),
    path(
        route='block',
        view=views.UserBlock.as_view(),
        name='block'),
    path(
        route='me/profile/blocked_users/<int:pk>',
        view=views.UserBlockedList.as_view(),
        name='blocked_users'),
    path(
        route='privacity',
        view=views.UserPrivacity.as_view(),
        name='privacity'),

    # Posts
    path(
        route='profile/<str:username>/',
        view=views.UserDetailView.as_view(),
        name='detail'
    )
]