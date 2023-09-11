from django.contrib import admin
from .models import NewUser
from django.contrib.auth.models import User
# Register your models here.

class NewUserAdmin(admin.ModelAdmin):
    pass
admin.site.register(NewUser,NewUserAdmin)

