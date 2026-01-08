from django.contrib import admin
from .models import Project, ContactMessage

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title','created_at','project_url')
    search_fields = ('title','description')

@admin.register(ContactMessage)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','email','created_at','read')
    list_filter = ('read',)
    search_fields = ('name','email','message')
