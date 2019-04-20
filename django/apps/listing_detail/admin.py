from django.contrib import admin
from dwaiter.django.admin import DisplayableAdmin, MetaDataAdmin
from solo.admin import SingletonModelAdmin

from . import models


@admin.register(models.ListingPage)
class ListingPageAdmin(SingletonModelAdmin):
    fieldsets = MetaDataAdmin.fieldsets


@admin.register(models.Item)
class ItemAdmin(DisplayableAdmin):
    list_display = ['title', 'publication_date'] + DisplayableAdmin.list_display

    fieldsets = [
        (None, {
            'fields': [
                'title',
                'content',
            ]
        }),
    ] + DisplayableAdmin.fieldsets
