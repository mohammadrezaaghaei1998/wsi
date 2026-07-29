from django.contrib import admin
from .models import Project

@admin.register(Project)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('category', 'project_name', 'title_project_name', 'client','year','role','description',)
    list_filter = ('created_at',)
   





 