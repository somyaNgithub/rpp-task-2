from django.contrib import admin
from .models import users


class UserAdmin(admin.ModelAdmin):
    list_display = ('First_Name','Last_Name','Gender','Email')


# Register your models here.
admin.site.register(users,UserAdmin)


