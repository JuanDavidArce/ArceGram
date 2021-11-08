"""Users URLs"""
#Djano
from django.urls import path

#View
from chat import views


urlpatterns=[

    path(
        route='',
        view=views.messages_page,
        name='chat'),
    path(
        route='threads',
        view=views.New_thread.as_view(),
        name='threads')


]
