# models.py

from solo.models import SingletonModel

class Example(SingletonModel):
    class Meta:
        verbose_name_plural = 'Example'


# admin.py

from solo.admin import SingletonModelAdmin

class ExampleAdmin(SingletonModelAdmin):
    pass


# view.py

instance = models.Example.get_solo()
