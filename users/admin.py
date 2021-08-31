"""User admin classes"""

#Django
from django.contrib import admin


#Models
from users.models import Profile

# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Profile admin"""
    list_display= ('pk','user','phone_number','website')
    list_display_links=('pk','user')
    list_editable= ('phone_number', 'website')
    search_fields= ('user__email','user__first_name', 'user__last_name', 'phone_number','user__username')
    list_filter= ('created','modified','user__is_active','user__is_staff')