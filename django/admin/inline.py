from django.contrib import admin


class PollInline(admin.TabularInline):
    model = Poll

class PollAdmin(admin.ModelAdmin)
    inlines = [PollInilne]


# Sortable

from grappelli.forms import GrappelliSortableHiddenMixin

class PollInline(GrappelliSortableHiddenMixin, admin.TabularInline):
    model = Poll
    sortable_field_name = 'order'
    extra = 0
