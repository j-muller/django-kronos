from django.contrib import admin
from kronos.models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ['name', 'last_execution']
    list_filter = ('name', )

admin.site.register(Task, TaskAdmin)