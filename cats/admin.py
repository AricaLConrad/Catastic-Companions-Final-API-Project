# Sources I Used:
# https://data-flair.training/blogs/django-admin-customization/
# https://www.section.io/engineering-education/customizing-django-admin/

from django.contrib import admin
# from django.contrib.auth.models import Group
from .models import Cat

# Shows more fields with each cat.
class listCatFields(admin.ModelAdmin):

    model = Cat
    list_display = ('name', 'age', 'gender', 'is_adopted', 'date_admitted_to_shelter')
    list_filter = ('date_admitted_to_shelter', 'is_adopted')

# Adds the Cat model.
admin.site.register(Cat, listCatFields)

# Removes the Groups because I do not need them.
# admin.site.unregister(Group)

# Changes the header from "Django administration" to "Catastic Companions."
admin.site.site_header = "Catastic Companions"
    