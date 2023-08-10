from django.contrib import admin

from . models import nameauthor,news

@admin.register(nameauthor)
class Admin(admin.ModelAdmin):
    list_display = ("author" ,)

@admin.register(news)
class Admin(admin.ModelAdmin):
    list_display = ("author", "headlines", "newscontent")
   
# Register your models here.
