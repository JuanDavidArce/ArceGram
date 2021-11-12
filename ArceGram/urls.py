"""ArceGram URLs module."""

"""ArceGram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#Django
from os import name
from django.conf.urls import include
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('admin/',admin.site.urls),
    path('',include(('posts.urls','posts'),namespace='posts')),
    path('chat/', include(('chat.urls','chat'), namespace='chat')),
    path('users/',include(('users.urls','users'),namespace='users')),

]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
admin.site.site_header = 'Administracion de ArceGram'
admin.site.site_title = 'Administracion de ArceGram'