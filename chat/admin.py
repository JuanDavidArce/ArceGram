from django.contrib import admin
from django import forms
from django.core.exceptions import ValidationError
from django.db.models import Q
from .models import Thread, ChatMessage



@admin.register(Thread)
class ThreadAdmin(admin.ModelAdmin):
    """Thread admin"""
    list_display= ('pk','first_person','second_person')
    list_display_links=('pk',)
    list_editable= ('first_person', 'second_person')
