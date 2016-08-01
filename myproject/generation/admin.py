from django.contrib import admin

from .models import Name

class NameAdmin(admin.ModelAdmin):
    fields= []

admin.site.register(Name)