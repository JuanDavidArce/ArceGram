from django.contrib import admin

from posts.models import Post
# Register your models here.

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Post admin"""
    list_display= ('pk','title','photo','created','modified')
    list_display_links=('pk','created','modified')
    list_editable= ('title', 'photo')

