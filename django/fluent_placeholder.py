# models.py

from django.db import models
from fluent_contents.models.fields import (PlaceholderField, ContentItemRelation, PlaceholderRelation)


class Penguin(models.Model):
    content = PlaceholderField('penguin_content', verbose_name='Content')
    contentitem_set = ContentItemRelation()
    placeholder_set = PlaceholderRelation()


# admin.py

from django.contrib import admin
from fluent_contents.admin import PlaceholderFieldAdmin


class PenguinAdmin(PlaceholderFieldAdmin, admin.ModelAdmin):
    pass


admin.site.register(models.Penguin, PenguinAdmin)
