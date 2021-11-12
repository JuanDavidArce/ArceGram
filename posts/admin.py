from django.contrib import admin

from posts.models import Post,Like,Comment
# Register your models here.

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Post admin"""
    list_display= ('pk','title','photo','created','modified')
    list_display_links=('pk','created','modified')
    list_editable= ('title', 'photo')

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    """Post admin"""
    list_display= ('pk','user','post')
    list_display_links=('pk',)
    list_editable= ('user', 'post')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """Post admin"""
    list_display= ('pk','user','comment','post')
    list_display_links=('pk',)
    list_editable= ('user','comment', 'post')
   
