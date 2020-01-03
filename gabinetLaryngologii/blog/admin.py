from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_date', 'published_time', 'published')
    list_filter = ('published', 'published_date')
    search_fields = ('title', 'long_text')
    date_hierarchy = 'published_date'
    ordering = ('published', 'published_date')
