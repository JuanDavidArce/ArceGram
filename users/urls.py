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

    #Posts
    path(
        route='profile/<str:username>/',
        view=views.UserDetailView.as_view(),
        name='detail'
    )
]