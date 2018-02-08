from django.contrib import admin

from . import models


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    model = models.Category


@admin.register(models.Anime)
class AnimeAdmin(admin.ModelAdmin):
    model = models.Anime

    prepopulated_fields = {'slug': ('name',)}


@admin.register(models.Ep)
class EpAdmin(admin.ModelAdmin):
    model = models.Ep

    prepopulated_fields = {'slug': ('title',)}
