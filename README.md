django-suit-sortable
====================

Drag-and-drop ordering for objects and inlines in Django admin using [django-suit](https://github.com/darklow/django-suit).

## Installation
	pip install -e git://github.com/JP74/django-suit-sortable.git#egg=suit_sortable

## Configuration

1. Add `suit_sortable` to your `INSTALLED_APPS`.
2. Ensure `django.core.context_processors.static` is in your `TEMPLATE_CONTEXT_PROCESSORS`.


To use suit_sortable you must do following:

In your ``models.py`` file add integer property for sortable to you model:

    from django.db import models

    class Category(models.Model):
        ...
        position = models.PositiveIntegerField()


### Adding Sortable to an existing model

If you're adding Sorting to an existing model, it is recommended that you use [django-south](http://south.areacode.com/) to create a schema migration to add the "position" field to your model. You will also need to create a data migration in order to add the appropriate values for the `position` column.

Example assuming a model named "Category":

    def forwards(self, orm):
        for index, category in enumerate(orm.Category.objects.all()):
            category.position = index + 1
            category.save()



### Django Admin Integration
To enable sorting in the admin, you need to inherit from `SortableAdmin`:

    from django.contrib import admin
    from myapp.models import MySortableClass
    from suit_sortable.admin import SortableAdmin

    class MySortableAdminClass(SortableAdmin):
        """Any admin options you need go here"""

    admin.site.register(MySortableClass, MySortableAdminClass)


To enable sorting on TabularInline models, you need to inherit from
SortableTabularInline:

    from suit_sortable.admin import SortableTabularInline

    class MySortableTabularInline(SortableTabularInline):
       """Your inline options go here"""


To enable sorting on StackedInline models, you need to inherit from
SortableStackedInline:

    from suit_sortable.admin import SortableStackedInline

    class MySortableStackedInline(SortableStackedInline):
       """Your inline options go here"""


### Limitations

Since sortables are based on JavaScript solution, there are known limitations:

1. It doesn't work with pagination.