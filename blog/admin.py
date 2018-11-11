from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status', 'created')
    list_filter = ('status', )

admin.site.register(Post, PostAdmin)
