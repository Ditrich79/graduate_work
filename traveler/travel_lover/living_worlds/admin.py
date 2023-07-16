from django.contrib import admin
from .models import Worlds


class WorldsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created', 'image')
    list_display_links = ('id', 'title')


admin.site.register(Worlds, WorldsAdmin)
