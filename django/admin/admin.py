from django.contrib import admin

from . import models


@admin.register(models.Penguin)
class PenguinAdmin(admin.ModelAdmin):
    list_display = ['title']

    fieldsets = [
        (None, {
            'fields': ['title', 'content'],
        }),
    ]
