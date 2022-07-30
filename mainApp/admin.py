from django.contrib import admin
from .models import Contact, project, Hire


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['cid','name','email','subject','message']

@admin.register(project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['pid','pName','pUrl','pImage']

@admin.register(Hire)
class HireAdmin(admin.ModelAdmin):
    list_display = ['Hid','name','email','subject','message']
