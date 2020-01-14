from django.contrib import admin
from .models import Media


@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ('media_name', 'media_description', 'extension')
    search_fields = ('media_name',)
    ordering = ('id',)


