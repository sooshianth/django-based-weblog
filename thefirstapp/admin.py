from django.contrib import admin
from .models import Post, Comment

class CommentAdminInline(admin.TabularInline):
    model = Comment
    fields = ['text', ]
    extra = 0

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'is_enabled', 'created_time', 'publish_time']
    inlines = [CommentAdminInline]

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'post', 'text', 'is_enabled', 'created_time']


# admin.site.register(Post, PostAdmin)
# admin.site.register(Comment, CommentAdmin)