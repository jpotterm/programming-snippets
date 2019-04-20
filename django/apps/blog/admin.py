from django.contrib import admin
from dwaiter.django.admin import DisplayableAdmin, MetaDataAdmin
from solo.admin import SingletonModelAdmin

from . import models


@admin.register(models.BlogListingPage)
class BlogListingPageAdmin(SingletonModelAdmin):
    fieldsets = MetaDataAdmin.fieldsets


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(models.Post)
class PostAdmin(DisplayableAdmin):
    list_display = ['title', 'category', 'publication_date'] + DisplayableAdmin.list_display

    fieldsets = [
        (None, {
            'fields': [
                'title',
                'category',
                'summary',
                'content',
            ]
        }),
    ] + DisplayableAdmin.fieldsets
