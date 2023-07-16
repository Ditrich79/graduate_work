from django.contrib import admin
from .models import Stories


class StoriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created', 'image')
    list_display_links = ('id', 'title')


admin.site.register(Stories, StoriesAdmin)

