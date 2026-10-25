from django.contrib import admin
from .models import Post
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "post_type", "game_name", "author", "status", "created_at", "views")
    list_filter = ("post_type", "status", "created_at")
    search_fields = ("title", "game_name", "excerpt", "content", "author__username")
    prepopulated_fields = {"slug": ("title",)}
