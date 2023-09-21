from django.contrib import admin

# Register your models here.
from .models import Describe
 
class LocalAdmin(admin.ModelAdmin):
 
    list_display = ("id", "description")

admin.site.register(Describe,LocalAdmin)
