from django.contrib import admin
from .models import Pet


@admin.register(
    Pet)  # the model admin has an attribute called list_display which we can use to list that we want to display
class PetAdmin(admin.ModelAdmin):
    list_display = ['name', 'species', 'breed', 'age', 'sex']
