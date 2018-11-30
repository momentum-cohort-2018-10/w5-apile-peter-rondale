from django.contrib import admin
from apile_app.models import Post, Comment

class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display = ('author', 'title', 'description', 'date_added',)
    prepopulated_fields = {'slug': ('slug',)}

class CommentAdmin(admin.ModelAdmin):
    model = Comment
    list_display = ('author', 'description', 'date_added',)

# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
