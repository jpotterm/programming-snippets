class MyModelAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'author':
            kwargs['initial'] = request.user.id
        return super(MyModelAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)
