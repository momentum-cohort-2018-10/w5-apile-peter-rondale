from django.contrib import admin
from apile_app.models import Post, Vote

class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display = ('author', 'title', 'description', 'date_added',)
    prepopulated_fields = {'slug': ('slug',)}

# Register your models here.
admin.site.register(Post, PostAdmin)
