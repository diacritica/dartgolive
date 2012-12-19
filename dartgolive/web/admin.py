from web.models import *
from django import forms
from django.contrib import admin
from django.contrib.admin.widgets import FilteredSelectMultiple


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Project, ProjectAdmin)
