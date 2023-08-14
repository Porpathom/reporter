from django.contrib import admin

from . models import Nameauthor,New

@admin.register(Nameauthor)
class Admin(admin.ModelAdmin):
    list_display = ("author" ,)

@admin.register(New)
class Admin(admin.ModelAdmin):
    list_display = ("author", "headlines", "newscontent")
    search_fields = ("author", "headlines", "newscontent")
   
# Register your models here.
