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


]