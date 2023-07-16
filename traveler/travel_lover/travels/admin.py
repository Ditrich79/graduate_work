from django.contrib import admin
from .models import Travels


class TravelsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'image')
    list_display_links = ('id', 'title')


admin.site.register(Travels, TravelsAdmin)

