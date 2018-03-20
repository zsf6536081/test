from django.contrib import admin
from .models import user
# Register your models here.

class useradmin(admin.ModelAdmin):
    list_display = ['username','password']

admin.site.register(user,useradmin)