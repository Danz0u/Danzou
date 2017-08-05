from django.contrib import admin
from core.models import *


@admin.register(Anime)
class AnimeAdmin(admin.ModelAdmin):
    model = Anime

    list_display = ('title', 'created_at', 'updated_at')
